def remove_leading_zeroes(ip_address):
    components = ip_address.split('.')
    formatted_components = [str(int(component)) for component in components]
    formatted_ip = '.'.join(formatted_components)
    return formatted_ip

input_ip = input("Enter an IP address: ")
formatted_ip = remove_leading_zeroes(input_ip)
print("Formatted IP address:", formatted_ip)
