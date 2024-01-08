default_settings = {'theme': 'light', 'font_size': 16}
user_settings = {'font_size': 20, 'show_avatar': True}

# merged_settings = {
#     **default_settings,
#     **user_settings
# }

merged_settings = default_settings | user_settings
print(merged_settings)