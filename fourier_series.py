import turtle
import math
import time
from collections import deque

class FourierSeries:
    def __init__(self,n,radius):
        self.number = n
        self.screen = turtle.Screen()
        self.screen.bgcolor('Green')
        turtle.screensize(canvwidth=1000, canvheight=500) 
        self.time = 0.01
        self.screen.tracer(0)
        self.wave = deque()
        self.radius = radius
         
    def draw(self):
        circles = {}
        circle_points = {}
        radii = {}
        ref_for_cps_x = {}
        ref_for_cps_y = {}
        vectors = {}
        for i in range(self.number):
            circles[f"circle{i+1}"] = turtle.Turtle()
            circles[f"circle{i+1}"].hideturtle()

            circle_points[f"circle_point_{i+1}"] = turtle.Turtle() 
            circle_points[f"circle_point_{i+1}"].speed(10)
            circle_points[f"circle_point_{i+1}"].penup()

            radii[f"radius_{i+1}"] = 0

            ref_for_cps_x[f"ref_for_cp_{i+1}"] = 0
            ref_for_cps_y[f"ref_for_cp_{i+1}"] = 0
       
        radius_sum = 0
        for i in range(self.number):
            n = i * 2 +1
            radius = self.radius * (4/ (n * (math.pi)))
            radius_sum += radius   
            print(radius)
            if i == 0:
                radii[f"radius_{i+1}"] = radius
                circles[f"circle{i+1}"].pendown() 
                circles[f"circle{i+1}"].circle(radius)
                circles[f"circle{i+1}"].penup()
                circles[f"circle{i+1}"].setpos(radius,radius)
            else:
                circles[f"circle{i+1}"].penup()
                circles[f"circle{i+1}"].setpos(radius_sum - radius,radii[f"radius_1"] - radius)    
                ref_for_cps_x[f"ref_for_cp_{i+1}"] = circles[f"circle{i}"].xcor()
                circles[f"circle{i+1}"].pendown()
                circles[f"circle{i+1}"].circle(radius)
                radii[f"radius_{i+1}"] = radius
                circles[f"circle{i+1}"].penup()
                circles[f"circle{i+1}"].setpos(radii[f"radius_{1}"],radii[f"radius_{1}"])
                self.screen.update()         

        wave_point = turtle.Turtle()
        wave_point.hideturtle()
        wave_point.penup() 
        wave_point.speed(0)     
        wave_point.pencolor("#363331") 
        wave_point.pensize(3) 

        radius_sum = 0    
        for i in range(self.number):
            n = i * 2 +1
            radius = self.radius * (4/ (n * (math.pi)))
            radius_sum += radius   
            vectors[f"vector_{i+1}"] = turtle.Turtle()
            vectors[f"vector_{i+1}"].penup()
            vectors[f"vector_{i+1}"].hideturtle()
            vectors[f"vector_{i+1}"].pensize(3) 
            vectors[f"vector_{i+1}"].pencolor("orange") 

          
   
        resultant = turtle.Turtle()
        resultant.hideturtle()
        resultant.penup()
        resultant.speed(10) 
        resultant.pencolor("blue") 
        resultant.pensize(3.4) 

        while True :
            x=0
            y=0
            self.time += 0.07
            count =0
            for i in range(self.number):
                circle_points[f"circle_point_{i+1}"].showturtle()

            for i in range (self.number):
                count+=1
                n = i * 2 + 1
                radius = self.radius * (4/ (n * (math.pi)))  
                prev_x = x
                prev_y = y
                 
                x += radius * math.cos(n * self.time)
                y += radius * math.sin(n * self.time)     
                circle_points[f"circle_point_{i+1}"].goto(x,y)
                self.move_circle(prev_x,prev_y,circles[f"circle{i+1}"],radii[f"radius_{i+1}"])
                
                self.draw_line(vectors[f"vector_{i+1}"],prev_x,prev_y,circle_points[f"circle_point_{i+1}"],count,self.time)
                self.screen.update()     
                
            self.wave.appendleft(y)
                
                
            self.draw_wave_point(wave_point)
            self.draw_vector(resultant,circle_points[f"circle_point_{self.number}"].xcor(),circle_points[f"circle_point_{self.number}"].ycor())
                  
                
            time.sleep(0.01)
                    
    def draw_line(self,vector,x,y,circle_point,count,time):
        vector.clear()
        vector.pendown()
        vector.speed(10)
        vector.goto(x,y)
        vector.penup()      
        time += 0.07
        xn = 0
        yn = 0
        for i in range(0,count):
            n = i * 2 + 1
            radius = self.radius * (4/ (n * (math.pi)))  
            xn += radius * math.cos(n * (time))
            yn += radius * math.sin(n * (time))       
        vector.goto(xn,yn) 
                           

    
    def move_circle(self,x1,y1,circle_2,radius):
        circle_2.clear()
        circle_2.speed(10) 
        circle_2.penup()
        circle_2.goto(x1,y1-radius)
        circle_2.pendown()
        circle_2.circle(radius)
            

    def draw_wave_point(self,wave_point):
        wave_point.goto(0+self.radius*2,self.wave[0])
        wave_point.dot()
        self.move_wave(wave_point)

    def draw_vector(self,resultant,x,y,height_correction=0):
        resultant.clear()
        resultant.goto(x,y)
        resultant.pendown()
        resultant.goto(0+self.radius*2,self.wave[0]+height_correction)
        resultant.penup()
        

    def move_wave(self,wave_point):
        wave_point.speed(0)
        wave_point.clear()
        for i in range(0,len(self.wave)):
            wave_point.goto(i+1+self.radius*2,self.wave[i])
            wave_point.dot()
          
f = FourierSeries(7,140)
f.draw()


