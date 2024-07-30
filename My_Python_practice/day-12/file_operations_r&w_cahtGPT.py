def update_server_config(file_path, key, value):
    try:
        # Read the existing content of the server configuration file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Flag to track if the key was found and updated
        key_found = False

        # Update the configuration value for the specified key
        with open(file_path, 'w') as file:
            for line in lines:
                # Check if the line starts with the specified key
                if line.startswith(key + "="):
                    # Update the line with the new value
                    file.write(key + "=" + value + "\n")
                    key_found = True
                else:
                    # Keep the existing line as it is
                    file.write(line)

            # If the key was not found, append it to the end of the file
            if not key_found:
                file.write(key + "=" + value + "\n")
                
        print(f"Configuration updated: {key} = {value}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"Error: An IOError occurred. Details: {e}")

# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '1075'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)

