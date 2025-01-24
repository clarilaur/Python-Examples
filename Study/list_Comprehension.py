# [expr for val in collection]
# [expr for val in collection if <test>]
# [expr for val in collection if <test> and <test2>]

movies1 = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone With the Wind",
           "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghost Busters",
           "To Kill a Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day",
           "Close Encounters of the Third Kind"]

movies2 = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946), ("Gattica",1997), ("No Country for Old Men",2007),
          ("Rear Window",1954), ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 1993),
          ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001), ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

gmovies = [title for title in movies1 if title.startswith('G')]
print(gmovies)

yearmovies = [title for (title,year) in movies2 if year<2000]
print(yearmovies)
