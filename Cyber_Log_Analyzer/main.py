success_count = 0
failed_count = 0

failed_ips = {}

def analyze_log():

    global success_count
    global failed_count
    global failed_ips

    file_name = input("Enter log file name: (example: monday.txt): ")

    try: 

        with open("logs/monday.txt") as file:

            for line in file:

                parts = line.split("|")

                time = parts[0].strip()
                ip_address = parts[1].strip()
                user_name = parts[2].strip()
                status = parts[3].strip()


                if status == "SUCCESS":
                    success_count += 1

                elif status == "FAILED":
                    failed_count += 1

                    if ip_address in failed_ips:
                        failed_ips[ip_address] += 1
            
                    else:
                        failed_ips[ip_address] = 1                


        print("\n===== ANALYSIS COMPLETE =====")
        print(f"Succssful logins: {success_count}")
        print(f"Failed logins: {failed_count}")
        print(failed_ips)


    except FileNotFoundError:
        print("Log file not found.")



def show_statistics():

    print("\n===== LOGIN STATISTICS =====")

    total_attempts = success_count + failed_count

    print(f"Total login Attempts : {total_attempts}")
    print(f"Success Logins : {success_count}")
    print(f"Failed Logins : {failed_count}")


def suspicious_activity():

    print("\n===== SUSPICIOUS ACTIVITY =====")

    suspicious_found = False

    for ip_address, count in failed_ips.items():

        if count >= 2:
            print(
                f"Suspicious IP : {ip_address}\n"
                f"Failed Attempts : {count}"
            )

            suspicious_found = True

    if suspicious_found == False:
        print("No suspicious activity detected.")


    
def generate_report(): 

    with open("security.txt", "w") as report:
        total_attempts = success_count + failed_count

        report.write("====== CYEBER SECURITY REPORT ======\n\n")

        report.write(
            f"Total Login Attempts: {total_attempts}\n"
        )

        report.write(
            f"Successful Logins: {success_count}\n"
        )

        report.write(
            f"Failed Logins : {failed_count}\n"
        )

        report.write("Failed Login Acitivity:\n")

        for ip_address, count in failed_ips.items():

            report.write(
                f"{ip_address} : {count} failed attempts\n"
            )
        
            report.write("\nSuspicious IP Addresses:\n")

            suspicious_found = False

        if suspicious_found == False:
            report.write("No suspicious activity detected.\n")

    print("Security report generated successfully.")



while True:

    print("\n===== CYBER LOG ANALYZER =====")

    print("1. Analyze Log File")
    print("2. Show Login Statistics")
    print("3. Detect Suspicious Activity")
    print("4. Generate Security Report")
    print("5. Exit")


    chose = input("Choose an option (1-5): ")


    if chose == "1":

        analyze_log()


    elif chose == "2":

        show_statistics()


    elif chose == "3":

        suspicious_activity()


    elif chose == "4":

        generate_report()


    elif chose == "5":

        print(
            "Thanks for using Cyber Log Analyzer.\n"
            "Exiting..."
        )

        break


    else:

        print("Wrong input. Choose from 1 to 5.")



    