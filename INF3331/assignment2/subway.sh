#!/usr/bin/env sh  

# Default station: Forskningsparken
metro_station_id='3010370'

# Default platform: 0
metro_platform_only=0

if [ $# -gt 0 ]; then
  for i in $@; do 
    case "${i}" in
      --W|--w)
        metro_platform_only=2
        ;;
      --E|--e)
        metro_platform_only=1
        ;;
      blindern|Blindern)
        metro_station_id='3010360'
        ;;
      vestli|Vestli)
        metro_station_id='3011730'
        ;;
      *)
        echo 'Unknown parameter or station. Abort.'
        exit 1
    esac
  done
fi

# Fetch the data
APIRETURN=$(curl -s "http://reisapi.ruter.no/StopVisit/GetDepartures/${metro_station_id}/?transporttypes=Metro")

# Split the data into an array
#IFS='MonitoredVehicleJourney' read -ra travel_data <<< "${APIRETURN}"
set -f #Disable * expansion

# Set a custom delimiter
# Bash replacement sucks here
not_json_data=$(echo ${APIRETURN} | sed -e "s/MonitoredVehicleJourney/###/g")

# Break up the string at the custom delimiter
IFS='\#\#\#' read -ra travel_data <<< "${not_json_data}"

for line in "${travel_data[@]}"; do

  # Reset variables
  metro_line=false
  metro_direction_name=false
  metro_destination_name=false
  metro_destination_ref=false
  metro_expected_departure_time=false

  # Metro line number
  PATTERN="LineRef\":\"([0-9])"
  if [[ $line =~ $PATTERN ]]; then
    metro_line=${BASH_REMATCH[1]}
  fi

  # Departure platform name and platform number
  PATTERN="DeparturePlatformName\":\"([0-9])(\ [^\"]+)\""
  if [[ $line =~ $PATTERN ]]; then
    metro_direction_name="${BASH_REMATCH[1]}${BASH_REMATCH[2]}"
    metro_destination_ref="${BASH_REMATCH[1]}"
  fi

  # Line Destination
  PATTERN="DestinationName\":\"([a-zA-Z\ ]+)\""
  if [[ $line =~ $PATTERN ]]; then
    metro_destination_name=${BASH_REMATCH[1]}
  fi

  # Departure Time (reformatted)
  PATTERN="ExpectedDepartureTime\":\"([0-9]{4}-[0-9]{2}-[0-9]{2})T([0-9\:]{5})"
  if [[ $line =~ $PATTERN ]]; then
    metro_expected_departure_time="${BASH_REMATCH[1]} ${BASH_REMATCH[2]}"
  fi

  # Output if a metro line has been found
  if [ $metro_line != false ] && \
     [[ $metro_direction_name ]] && \
     [[ $metro_destination_ref ]] && \
     [[ $metro_destination_name ]] &&  \
     [[ $metro_expected_departure_time ]]; then
      if [ $metro_platform_only = 0 ] || [ $metro_platform_only = $metro_destination_ref ]; then
        echo "$metro_expected_departure_time : Line: $metro_line, platform $metro_direction_name, $metro_destination_name"
      fi
    fi
done
