import validator_collection
def main():
    ans=validator_collection.is_email(input("What's your email address? "))
    if ans:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()