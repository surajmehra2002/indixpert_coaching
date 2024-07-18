vots ={1 : "suraj",
       2 : "vimal",
       3 : "gaurav",
       4 : "nisha",
       5 : "tanuja"
    }
hitech ={6 : "anand",
       7 : "faiz",
       8 : "mazda",
       9 : "Roshni",
       10 : "amit",
       11 : "indra"
    }


# print(vots)
# print(hitech)

Students = vots.copy()
Students.update(hitech)
# for key, value in hitech.items():
#     Students[key] = value

print(Students)