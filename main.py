def quiz(dict):
  score=0
  for quns,ans in dict.items():
    print(quns)
    for option in ans[0]:
      print(option)
    usr_input=input("your opition\n")
    if ( usr_input==ans[1]):
      score=score+1
      print("wow you are right...!")
    else:
      print("oops wrong answer")
  print("your total score is "+str(score)+"/10")
  if(score >= 8):
    print("yipee you are my best friend...! Thank you "+name)
  elif(4>= score <8):
    print("okay, we need to chat more..!Thank you "+name)
  else:
    print("you need to knw more about me...! Thank you "+name)

name=input("Enter your name\n")
print("hello "+ name +"..! Welcome to my quiz:")
print("I want to know that how well you know about me....so lets start the game..!\n My 1st question is")
dict={"1.What food does chetana hate?":[["a.cheese","b.Tomatoes","c.cake","d.Pizza"],"b"],"2.What talent does chetana have?":[["a.Dancing","b.Singing","c.Drawing","d.Reading"],"a"],"3.What type of movies does chetana like?":[["a.Romance","b.comedy","c.Horror","d.Fantasy"],"c"],"4.How tall am I?":[["a.5.5","b.5.6","c.5.7","d.5.8"],"c"],"5.Chetana's Fvrt colour?":[["a.Blue","b.Black","c.Red","d.Yellow"],"b"],"6.Which fast food restaurant does chetana prefer the most?":[["a.McDonalds","b.KFC","c.subway","d.pizza"],"b"],"7.Which animal does chetana dream to pet?":[["a.Dog","b.Cat","c.Rabbit","d. A bird"],"a"],"8.Where would chetana like to go with her soulmate?":[["a.Paris","b.Maldives","c.Leh ladakh","d.Venice"],"c"],"9.chetana's fvrt ice cream flavor?":[["a.vanilla","b.chocolate","c.black current","d.strawberry"],"c"],"10.chetana's date of birth":[["a.2","b.5","c.28","d.10"],"a"]}
quiz(dict)