import mysql.connector
from subprocess import call
from time import sleep
import sys
def clear():
    _ = call('clear')
cust_id=""
cart=[]
con = mysql.connector.connect(host="localhost", database="mystical_moo", user="root", password="O!9Thy3=")
cur=con.cursor(buffered=True)
print("Welcome to mystical moo")
def start():
    def admin_saaab():
        g=int(input("1.View Analytics\n2.Exit\nOption: "))
        if g==1:
            m=int(input("1.View the money spent by customers\n2.Show number of items in a particular category\n3.Show count of each payment method\noption"))
            if m==1:
                s="Select inv_cust_id,Sum(inv_price) as Total_Sales from Invoice Group by inv_cust_id with ROLLUP"
                cur.execute(s)
                f=cur.fetchall()
                print("ID     Price")
                for x in f:
                    print(*x,sep="     ")
                sleep(5)
                clear()
                admin_saaab()
            if m==2:
                l=0
                while(True):
                    l=int(input("Number of categories you would to search: "))
                    if(0<l<7):
                        break
                s="SELECT "
                c=["Camel","Buffalo","Goat","Cow","Yak","Horse","Donkey"]
                e=""
                for i in range(0,l-1):
                    h=""
                    while (h not in c):
                        h=input("Give Category:")
                    c.remove(h)
                    d="SUM(CASE WHEN type = \'"+h+"\' THEN quantity ELSE 0 END) AS "+h+" ,"
                    e+=h+"       "
                    s+=d
                h=""
                while (h not in c):
                    h=input("Give Category:")
                d="SUM(CASE WHEN type = \'"+h+"\' THEN quantity ELSE 0 END) AS "+h+" From inventory"
                e+=h+"  "
                s+=d
                cur.execute(s)
                fgh=cur.fetchall()
                print(e)
                for x in fgh:
                    print(*x,sep=" ")
                sleep(5)
                clear()
                admin_saaab()
            if m==3:
                s="select inv_payment_type, count(inv_cust_id) from Invoice group by inv_payment_type"
                cur.execute(s)
                fgh=cur.fetchall()
                for x in fgh:
                    print(*x,sep=" ")
                sleep(5)
                clear()
                admin_saaab()
        if g==2:
            sleep(0.5)
            clear()
            start()


    def Customer_page():
        print("Customer "+cust_id+"'s page")
        print("1.View previous orders\n2.View Invoices\n3.View Shipping details\n4.Exit")
        g=0
        while(True):
            g=int(input("Option: "))
            if (0<g<5):
                break
        if g==1:
            s="Select order_id, order_price,order_payment, order_status from Orders where order_cust_id="+cust_id
            cur.execute(s)
            f=cur.fetchall()
            Sno=1
            print("Sno.  Id   Price  Payment  Status")

            for x in f:
                print(Sno,end=" ")
                print(*x,sep=",    ")
                Sno+=1
            m=0
            m=int(input("1.Show Details\n2.Go back\noption:"))
            if m==1:
                while (True):
                    dfs=int(input("Give Sno."))
                    if (0<dfs<Sno):
                        s="select inventory.name, inventory.type,buggu.order_product_id,buggu.order_product_quantity ,buggu.order_order_id from (select * from OrderProduct where order_order_id="+str(f[dfs-1][0])+" )buggu join inventory on buggu.order_product_id=inventory.product_id;"
                        cur.execute(s)
                        bv=cur.fetchall()
                        print("Price  Name          Type     ProductID     Quantity        OrderID ")
                        print(f[dfs-1][1],end=" ")
                        print(*bv[0],sep=" ")
                        sleep(10)
                        clear()
                        Customer_page()
                        break
            if m==2:
                sleep(0.5)
                clear()
                Customer_page()
        if g==2:
            s="Select * from Invoice where inv_cust_id="+cust_id
            cur.execute(s)
            f=cur.fetchall()
            print("GST_ID                             date        Price      Payment         CustomerID   Order ID")
            for x in f:
                print(*x,sep=" ")
            sleep(10)
            clear()
            Customer_page()
        if g==3:
            s="Select * from Shipping_Details where shi_cust_id="+cust_id
            cur.execute(s)
            f=cur.fetchall()
            print("date_order     date_fullfill     Payment_Type   CustomerID     OrderID")
            for x in f:
                print(*x,sep=" ")
            sleep(10)
            clear()
            Customer_page()
        if g==4:
            sleep(0.5)
            clear()
            main_page()

    def main_page():
        print("Welcometo mystical moo customer "+cust_id)
        l=-1
        print("1.View Catalogue\n2.Order from Catalogue\n3.View Cart\n4.Customer Page\n5.exit")
        while(l>5 or l<0):
            l=int(input("Your option:"))
        sleep(0.5)
        clear()
        if l==1:
            view_catalogue()
        if l==2:
            order_screen()
        if l==3:
            view_cart()
        if l==4:
            Customer_page()
        if l==5:
            start()
    def view_cart():
        if (len(cart)==0):
            print("Cart is empty")
            sleep(0.5)
            clear()
            main_page()
        else:
            fds=1
            for i in cart:
                print("Sno. "+str(fds))
                s="select * from inventory where product_id ="+str(i[0])
                cur.execute(s)
                f=cur.fetchall()
                print("ID: "+str(f[0][0])+"\nName: "+str(f[0][1])+"\nPrice: "+str(f[0][4])+"\nQuantity taken: "+str(i[1]))
                fds+=1
            print("1.Proceed to checkout\n2.Delete items\n3.Adjust Quantity\n4.Go back")
            while(True):
                g=int(input("Give option: "))
                if (0<g<4):
                    break
            if g==1:
                c=["Cash","Pre-Paid","Post-payment"]
                d=["Fulfilled","Placed"]
                hh=""
                while (hh not in c):
                    hh=input("Enter payment type "+"Cash "+"Pre-Paid "+"Post-payment "+"(Case Sensitive)")
                order_q="Insert into orders(order_cust_id,order_coupon_id,order_price,order_payment,order_status) values("+cust_id+", null,"+str(0)+", \'"+hh+"\', \'"+d[1]+"\' )"
                cur.execute(order_q)
                prooce=0
                cur.execute("SELECT * FROM orders ORDER BY order_id DESC LIMIT 1")
                lund=cur.fetchall()
                for j in (cart): #no. of prods
                    lur=con.cursor(buffered=True)
                    OrderProd_q="Insert into OrderProduct(order_product_quantity,order_order_id,order_product_id) values("+str(j[1])+", "+str(lund[0][0])+", "+str(j[0])+" )"
                    lur.execute(OrderProd_q)
                    pricequery="Select price, discount from inventory where product_id="+str(j[0])
                    lur.execute(pricequery)
                    fgh=lur.fetchall()
                    prooce+=j[1]*fgh[0][0]*((100-fgh[0][1])/100)
                updatequery="update orders set order_price="+str(prooce)+" where order_id="+str(lund[0][0])
                cur.execute(updatequery)
                print("Order Placed")
                cart.clear()
                sleep(0.5)
                clear()
                main_page()
            elif g==2:
                df=0
                while(True):
                    df=int(input("give the Sno. of the product you will delete"))
                    if(0<df<fds):
                        del cart[df-1]
                        print("Item deleted")
                        break
                sleep(1)
                clear()
                print("New Updated Cart: ")
                view_cart()         
            elif g==3:
                df=0
                while(True):
                    df=int(input("give the Sno. of the product you will change the quantity of"))
                    if(0<df<fds):
                        while (True):
                            d=int(input("Enter new Quantity(maximum 10)"))
                            if (0<d<10):
                                break
                        cart[df-1][1]=d
                        print("Item Quantity updated")
                        break
                sleep(1)
                clear()
                print("New Updated Cart: ")
                view_cart()         

            elif g==4:
                sleep(0.5)
                clear()
                main_page()
    def product_page():
    
        while(True):
            product_id=int(input("Which product would you like to see(id): "))
            if(0<product_id<99):
                break
        s="select * from inventory where product_id ="+str(product_id)
        cur.execute(s)
        f=cur.fetchall()
        print("ID: "+str(f[0][0])+"\nName: "+str(f[0][1])+"\nDescription: "+str(f[0][2])+"\nRating: "+str(f[0][3])+"\nPrice: "+str(f[0][4])+"\nDiscount%: "+str(f[0][5])+"\nType: "+str(f[0][6])+"\nStock: "+str(f[0][7]))
        g=int(input("1.Add to cart\n2.Go back"))
        if g==1:
            while (True):
                    d=int(input("Enter Quantity(maximum 10)"))
                    if (0<d<10):
                        break
            cart.append([product_id,d])
            print("Product added to cart")
            sleep(0.5)
            clear()
            order_screen()
        else:
            sleep(0.5)
            clear()
            order_screen()
    def order_screen():
        c=["Camel","Buffalo","Goat","Cow","Yak","Horse","Donkey","Exit"]
        print(*c,sep=" ")
        l=""
        while(l not in c):
            l=input("Choose category from above(Case sensitive): ")
            if l=="Exit":
                sleep(0.5)
                clear()
                main_page()
        sdf=0
        while(True):
            sdf=int(input("Enter inclusive lower price range (3-9): "))
            if (2<sdf<10):
                break
        s="select product_id, name , price from inventory where type = \'"+l+"\' and price >="+str(sdf)
        cur.execute(s)
        f=cur.fetchall()
        print("Poduct id, Name, Price:")
        for j in f:
            print(*j,sep=" ")
        g=int(input("1.Continue Browsing\n2.Go to specific product page\noption:"))
        if g==1:
            sleep(0.5)
            clear()
            order_screen()
        else:
            sleep(0.5)
            clear()
            product_page()
    def view_catalogue():
        c=["Camel","Buffalo","Goat","Cow","Yak","Horse","Donkey","Exit"]
        print(*c,sep=" ")
        l=""
        while(l not in c):
            l=input("Choose category from above(Case sensitive): ")
            if l=="Exit":
                sleep(0.5)
                clear()
                main_page()
        sdf=0
        while(True):
            sdf=int(input("Enter inclusive lower price range (3-9): "))
            if (2<sdf<10):
                break
        s="select product_id, name , price from inventory where type = \'"+l+"\' and price >="+str(sdf)
        cur.execute(s)
        f=cur.fetchall()
        print("Poduct id, Name, Price:")
        for j in f:
            print(*j,sep=" ")
        view_catalogue()
    def login_page():
        l=-1
        while(True):
            l=int(input("Give valid customer id: "))
            if 0<l<101:
                global cust_id
                cust_id=str(l)
                break
        s="Select Passwd from customer where id="+str(l)
        cur.execute(s)
        f=cur.fetchall()
        while(True):
            l=input("Give valid password:")
            if str(l)==f[0][0]:
                break
        sleep(0.5)
        clear()
        main_page()
    while(True):
        print("1.Customer Login\n2.Admin login\n3.exit\n")
        g=int(input("Option: "))
        if g==1:
            login_page()
        if g==2:
            h=""
            while(h!="Admin"):
                h=input("Login: ")
            h=""
            while(h!="Admin"):
                h=input("Password: ")
            admin_saaab()
        if g==3:
            sleep(0.5)
            clear()
            print("Program exited")
            con.commit()
            exit()
start()