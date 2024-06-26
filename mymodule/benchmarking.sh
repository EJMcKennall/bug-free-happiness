#! /usr/bin/env bash
# Run the given command as a background process and hide output
"$@" &>/dev/null &
# Capture the process id of the above process
pid="$!"
# Quit this script if someone presses Ctrl+C
trap exit SIGINT
# Print the top output including header info
top -pid "$pid"
# Check if the program is still running
while ps -p "$pid" > /dev/null ; do
    # Get the top info for this process
    top -pid "$pid" | tail -n +8 | head -1
    # Sleep for 0.2 seconds before the next output
    sleep 0.2
done

