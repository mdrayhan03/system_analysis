from datetime import date

rider = {
    "first_name" : "MD. Rafiq" ,
    "last_name" : "Khan" ,
    "email" : "rafiqkhan@gmail.com" ,
    "pN" : "01312961737" ,
    "gender" : "Male" ,
    "nid" : "4850163598" ,
    "dob" : date(1988, 1, 13).isoformat() ,
    "age" : f"{int(((date.today() - date(1988, 1, 13)).days) / 365.25)}",
    "password" : "1234" ,
    "type" : "Rider" ,
}

driver = {
    "first_name" : "MD. Kalam" ,
    "last_name" : "Hosen" ,
    "email" : "kalam@gmail.com" ,
    "pN" : "01641058157" ,
    "gender" : "Male" ,
    "nid" : "7810689615" ,
    "licence" : "DK21561385L57560" ,
    "dob" : date(1976, 5, 8).isoformat() ,
    "age" : f"{int(((date.today() - date(1976, 5, 8)).days) / 365.25)}",
    "password" : "1234" ,
    "type" : "Driver" ,
}