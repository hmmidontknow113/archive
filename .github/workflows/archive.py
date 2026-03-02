from savepagenow import capture

capture(
    "https://robey100.com",
    authenticate=True,
    capture_all=True
)

print("Archive complete")
