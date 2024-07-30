# Function definition to update the server configuration file
def update_server_config(file_path, key, value):
    try:
        # Read the existing contents of the server configuration file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Falg to track the if the Key was found and updated
        key_found = False

        # update the server configuration value for the specified key
        with open(file_path, 'w') as file:
            for line in lines:
                # check if the line starts with the specified key
                if line.startswith(key + "="):
                    # Update the value for the specified key
                    file.write(key + "=" + value + "\n")
                    key_found = True
                else:
                    # write the contents as it is
                    file.write(line)
            
            # If specified key not found: append it to the end of file
            if not key_found:
                file.write("\n"+ key + "=" + value)
        
        # print the info about update
        print(f"Configuration Updated: {key} = {value}")
    
    except FileNotFoundError:
        print(f"Error: file path {file_path} was not found")
    except IOError as e:
        print(f"IOError ocuured: {e}")

# Server Configuration file path
server_config_file_path = "server.conf"

# Key and values to update
key_to_update = "MAX_CONNECTIONS"
value_to_update = "600"

# update the server configuration file
update_server_config(server_config_file_path, key_to_update, value_to_update)