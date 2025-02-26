def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    result = ""
    units = [
        (31536000, "year"),
        (86400, "day"),
        (3600, "hour"),
        (60, "minute"),
        (1, "second")
    ]

    for u in units:
        if seconds < u[0]:
            continue
        else:

            t =  seconds // u[0]
            seconds = seconds % u[0]

            print(u, seconds)
            if result != "":
                if seconds == 0: 
                    sep = " and "
                else: 
                    sep = ", "
            else:
                sep = ""
            result += f"{sep}{t} {u[1]}{'s' if t > 1 else ''}"

    return result
def main():
    print(format_duration(62))

main()
