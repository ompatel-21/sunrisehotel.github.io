from flask import Flask,request,render_template,redirect,session,url_for
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="regestration"
)

app=Flask(__name__)
app.secret_key="123"

@app.route("/")
def index():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("index.html", n=n)
    else:
        return render_template("index.html")

@app.route("/in")
def ind():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='"+no+"'")
        data = mycur.fetchall()
        print("data:" ,data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("in.html", n=n)
    else:
        return render_template("rege.html")



@app.route("/insert",methods=['POST','GET'])
def insert():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        mycu = mydb.cursor()
        mycu.execute("INSERT INTO `login`(`username`, `email`, `password`) VALUES ('"+username+"','"+email+"','"+password+"')")
        mydb.commit()
        return redirect("/login")
    except Exception as e:
        return str(e)




@app.route("/reg")
def reg():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("reg.html", n=n)
    else:
        return render_template("reg.html")

@app.route("/about-us")
def aboutus():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("about-us.html", n=n)
    else:
        return render_template("about-us.html")

@app.route("/blog")
def blog():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("blog.html", n=n)
    else:
        return render_template("blog.html")

@app.route("/blog-no-sidebar")
def blognosidebar():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("blog-no-sidebar.html", n=n)
    else:
        return render_template("blog-no-sidebar.html")


@app.route("/blog-sidebar-left")
def blogsiderleft():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("blog-sidebar-left.html", n=n)
    else:
        return render_template("blog-sidebar-left.html")


@app.route("/blog-sidebar-right")
def blogsiderright():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("blog-sidebar-right.html", n=n)
    else:
        return render_template("blog-sidebar-right.html")


@app.route("/blog-single")
def blogsingle():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("blog-single.html", n=n)
    else:
        return render_template("blog-single.html")


@app.route("/blog-single-gallery")
def blogsinglegallery():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("blog-single-gallery.html", n=n)
    else:
        return render_template("blog-single-gallery.html")


@app.route("/contact")
def contact():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("contact.html", n=n)
    else:
        return render_template("contact.html")


@app.route("/event-single")
def eventsingle():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("event-single.html", n=n)
    else:
        return render_template("event-single.html")


@app.route("/event-single-expired")
def eventsingleexpired():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("event-single-expired.html", n=n)
    else:
        return render_template("event-single-expired.html")


@app.route("/events")
def events():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("events.html", n=n)
    else:
        return render_template("events.html")


@app.route("/events-2columns")
def events2columns():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("events-2columns.html", n=n)
    else:
        return render_template("events-2columns.html")


@app.route("/gallery")
def gallery():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("gallery.html", n=n)
    else:
        return render_template("gallery.html")


@app.route("/gallery-2columns1")
def gallery2columns1():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("gallery-2columns1.html", n=n)
    else:
        return render_template("gallery-2columns1.html")


@app.route("/gallery-full-width")
def galleryfullwidth():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("gallery-full-width.html", n=n)
    else:
        return render_template("gallery-full-width.html")


@app.route("/gallery-with-content")
def gallerywithcontent():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("gallery-with-content.html", n=n)
    else:
        return render_template("gallery-with-content.html")


@app.route("/gallery-without-filter")
def gallerywithoutfilter():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("gallery-without-filter.html", n=n)
    else:
        return render_template("gallery-without-filter.html")


@app.route("/index-2")
def index2():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("index-2.html", n=n)
    else:
        return render_template("index-2.html")


@app.route("/index-3")
def index3():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("index-3.html", n=n)
    else:
        return render_template("index-3.html")


@app.route("/index-4")
def index4():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("index-4.html", n=n)
    else:
        return render_template("index-4.html")


@app.route("/room")
def room():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("room.html", n=n)
    else:
        return render_template("room.html")





@app.route("/rooms")
def rooms():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='"+no+"'")
        data = mycur.fetchall()
        print("data:" ,data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("rooms.html", n=n)
    else:

        return render_template("rooms.html")


@app.route("/rooms-grid")
def roomsgrid():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("rooms-grid.html", n=n)
    else:
        return render_template("rooms-grid.html")


@app.route("/rooms-grid-2")
def roomsgrid2():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
        mycup=mydb.cursor()
        mycup.execute("SELECT * FROM product")
        pdata=mycup.fetchall()
        print("Name:", n)
        return render_template("rooms-grid-2.html", n=n,pdata=pdata)
    else:
        mycup = mydb.cursor()
        mycup.execute("SELECT * FROM product")
        pdata = mycup.fetchall()
        return render_template("rooms-grid-2.html", pdata=pdata)


@app.route("/room-single?<noo>")
def roomsingle(noo):
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            mycup = mydb.cursor()
            mycup.execute("SELECT * FROM product where pno='"+noo+"'")
            pdata = mycup.fetchall()
            print("Name:", n)
        return render_template("room-single.html", n=n,pdata=pdata)
    else:
        print(noo)
        mycup = mydb.cursor()
        mycup.execute("SELECT * FROM product where pno='"+noo+"'")
        pdata = mycup.fetchall()
        return render_template("room-single.html",pdata=pdata)


@app.route("/shop")
def shop():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            mycup = mydb.cursor()
            mycup.execute("SELECT * FROM restaurant")
            pdata = mycup.fetchall()
            print("Name:", n)
        return render_template("shop.html", n=n,pdata=pdata)
    else:
        mycup = mydb.cursor()
        mycup.execute("SELECT * FROM restaurant")
        pdata = mycup.fetchall()
        return render_template("shop.html",pdata=pdata)

@app.route("/shop-ajax")
def shopajax():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("shop-ajax.html", n=n)
    else:
        return render_template("shop-ajax.html")

@app.route("/shop-single")
def shopsingle():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("shop-single.html", n=n)
    else:
        return render_template("shop-single.html")

@app.route("/were-launching-soon")
def werelaunchingsoon():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("were-launching-soon.html", n=n)
    else:
        return render_template("were-launching-soon.html")

@app.route("/404")
def four():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("404.html", n=n)
    else:
        return render_template("404.html")

@app.route("/login")
def login():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("login.html", n=n)
    else:
        return render_template("login.html")

@app.route("/forgot")
def forgotpassword():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("forgot-password.html", n=n)
    else:
        return render_template("forgot-password.html")

@app.route("/rege")
def rege():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("register.html", n=n)
    else:
        return render_template("register.html")

@app.route("/log",methods=['GET','POST'])
def log():
    try:
        email=request.form['email']
        password=request.form['password']
        mycu=mydb.cursor()
        mycu.execute("SELECT * FROM `login` WHERE login.email='"+email+"' and login.password='"+password+"'")
        data=mycu.fetchall()
        if data==[]:
            return"username and password wrong"
        else:
            for row in data:
                session['no']=row[0]
                return redirect("/in")
    except Exception as e:
        return(str(e))

@app.route("/logout")
def logout():
    if 'no' in session:
        session.pop('no',None)
        return redirect("/")
    else:
        return redirect("/")

@app.route("/index2")
def index22():
    return render_template("/admin/index2.html")

@app.route("/table-datatable-basic")
def database():
    return render_template("/admin/table-datatable-basic.html")

@app.route("/guest-list")
def guestlist():
    mycu=mydb.cursor()
    mycu.execute("select * from cust_info")
    logindata=mycu.fetchall()
    return render_template("/admin/guest-list.html",logindata=logindata)

@app.route("/admin")
def admin():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from admin where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("/admin/admin.html", n=n)
    else:
        return render_template("/admin/admin.html")

@app.route("/adminlog",methods=['GET','POST'])
def adminlog():
    try:
        email=request.form['email']
        password=request.form['password']
        mycu=mydb.cursor()
        mycu.execute("SELECT * FROM `admin` WHERE admin.email='"+email+"' and admin.password='"+password+"'")
        data=mycu.fetchall()
        if data==[]:
            return"username and password wrong"
        else:
            for row in data:
                session['no']=row[0]
                return redirect("/index2")
    except Exception as e:
        return(str(e))

@app.route("/addadmin",methods=['GET','POST'])
def addadmin():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        mycu = mydb.cursor()
        mycu.execute("INSERT INTO `admin`(`username`, `email`, `password`) VALUES ('" + username + "','" + email + "','" + password + "')")
        mydb.commit()
        return redirect("/admin")
    except Exception as e:
        return str(e)

@app.route("/roominsert",methods=['POST','GET'])
def roominsert():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        room_type = request.form['room_type']
        room_price = request.form['room_price']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']
        mycu = mydb.cursor()
        mycu.execute("INSERT INTO `cust_info`(`name`, `email`, `phone`, `address`, `room_type`, `room_price`, `check_in_date`, `check_out_date`) VALUES ('"+name+"','"+email+"','"+phone+"','"+address+"','"+room_type+"','"+room_price+"','"+check_in_date+"','"+check_out_date+"')")
        mydb.commit()
        return redirect("/congrats")
    except Exception as e:
        return str(e)

@app.route("/contactinsert",methods=['POST','GET'])
def contactinsert():
    try:
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        mycu = mydb.cursor()
        mycu.execute("INSERT INTO `contact_us`(`username`, `email`, `phone`, `message`) VALUES ('"+username+"','"+email+"','"+phone+"','"+message+"')")
        mydb.commit()
        return redirect("/contact")
    except Exception as e:
        return str(e)

@app.route("/congrats")
def congrats():
    if 'no' in session:
        no = str(session['no'])
        print(no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
            print("Name:", n)
        return render_template("congrats.html", n=n)
    else:
        return render_template("congrats.html")

# @app.route("/cart")
# def cart():
#     if 'no' in session:
#         no = str(session['no'])
#         print(no)
#         mycur = mydb.cursor()
#         mycur.execute("select * from login where no='" + no + "'")
#         data = mycur.fetchall()
#         print("data:", data)
#         for row in data:
#             n = row[1]
#             print("Name:", n)
#         return render_template("cart.html", n=n)
#     else:
#         return render_template("cart.html")

@app.route("/cart")
def cart():
    if 'no' in session:
        no = str(session['no'])
        print("DATA of Session:",no)
        mycur = mydb.cursor()
        mycur.execute("select * from login where no='" + no + "'")
        data = mycur.fetchall()
        print("data:", data)
        for row in data:
            n = row[1]
        mycup=mydb.cursor()
        mycup.execute("select * FROM cart_data WHERE cart_data.cuno='"+no+"'")
        pdata=mycup.fetchall()
        print("Name:", n)
        return render_template("cart.html", n=n,pdata=pdata)
    else:
        # mycup = mydb.cursor()
        # mycup.execute("SELECT * FROM cust_info")
        # pdata = mycup.fetchall()
        return redirect("/")

if __name__ == "__main__":
    app.run(port=3000)