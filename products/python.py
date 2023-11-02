a = int(input("enter a number to check whether palindrome:"))
a=n
while(a>0){
    r=a%10
    rev=rev*10+r
    a=a/10

}
if(rev==n):
    print("number is palindrome")
