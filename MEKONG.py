import math
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import animation

'''
Overview: 
This is code for the Van-Der-Pol osciallator developed by the electrical
engineer and physicist Balthasar van der Pol. The differential equation is 
of the form 
            x''(t) - mu(1-x**2) x'(t) + x = 0 
    or      x''(t) = mu(1-x^2)x'(t) - x(t)

   and      y''(t) = -mu(1-x^2)y'(t)-y(t)

For the equation, we are going to express them as a system of first order 
linear equations. Let us start with x''(t):
        x''(t) = mu(1-x^2)x'(t) - x(t).
Let 
        Px=x(t), Vx= x'(t). 

Then, 
        Px'(t) = Vx
        Vx'(t) = mu(1-Px**2)Vx-Px
For the equation 

            y''(t) = -mu(1-x^2)y'(t)-y(t)

            Py=y(t), Vy=p'(t)
            Py'(t) = Vy
            Vy'(t)=-mu(1-Px**2)Vy-Py
'''
#Constants
mu=0.85
trail_length=5

class VanDerPol:
    def __init__(self,t,Px,Py,Vx,Vy):
        self.t=t
        self.Px=Px
        self.Py=Py
        self.Vx=Vx
        self.Vy=Vy
        
    def Fx(self,t,Px,Py,Vx,Vy):
        return Vx
    def Gx(self,t,Px,Py,Vx,Vy):
        return (mu*(1-(Px**2))*Vx)-Px
    def Fy(self,t,Px,Py,Vx,Vy):
        return Vy
    def Gy(self,t,Px,Py,Vx,Vy): 
        return (mu*(1-(Px**2))*Vy)-Py
        
    def UpdatePositionVelocity(self):
        n=10000
        t=self.t
        h=0.1
        Px=self.Px
        Vx=self.Vx
        Py=self.Py
        Vy=self.Vy

        T=[]
        X=[]
        Y=[]
        for i in range(n): 
            j1=self.Fx(t,Px,Py,Vx,Vy)
            k1=self.Gx(t,Px,Py,Vx,Vy)
            l1=self.Fy(t,Px,Py,Vx,Vy)
            m1=self.Gy(t,Px,Py,Vx,Vy)

            j2=self.Fx(t+(h/2),Px+(j1*h/2),Py+(h*k1/2),Vx+(h*l1/2),Vy+(h*m1/2))
            k2=self.Gx(t+(h/2),Px+(j1*h/2),Py+(h*k1/2),Vx+(h*l1/2),Vy+(h*m1/2))
            l2=self.Fy(t+(h/2),Px+(j1*h/2),Py+(h*k1/2),Vx+(h*l1/2),Vy+(h*m1/2))
            m2=self.Gy(t+(h/2),Px+(j1*h/2),Py+(h*k1/2),Vx+(h*l1/2),Vy+(h*m1/2))
            
            j3=self.Fx(t+(h/2),Px+(j2*h/2),Py+(h*k2/2),Vx+(h*l2/2),Vy+(h*m2/2))
            k3=self.Gx(t+(h/2),Px+(j2*h/2),Py+(h*k2/2),Vx+(h*l2/2),Vy+(h*m2/2))
            l3=self.Fy(t+(h/2),Px+(j2*h/2),Py+(h*k2/2),Vx+(h*l2/2),Vy+(h*m2/2))
            m3=self.Gy(t+(h/2),Px+(j2*h/2),Py+(h*k2/2),Vx+(h*l2/2),Vy+(h*m2/2))
            
            j4=self.Fx(t+h,Px+(j3*h),Py+(k3*h),Vx+(l3*h),Vy+(m3*h))
            k4=self.Gx(t+h,Px+(j3*h),Py+(k3*h),Vx+(l3*h),Vy+(m3*h))
            l4=self.Fy(t+h,Px+(j3*h),Py+(k3*h),Vx+(l3*h),Vy+(m3*h))
            m4=self.Gy(t+h,Px+(j3*h),Py+(k3*h),Vx+(l3*h),Vy+(m3*h))

            Vx+=(h/6)*(k1+(2*k2)+(2*k3)+k4)
            Vy+=(h/6)*(m1+(2*m2)+(2*m3)+m4)
            Px+=(h/6)*(j1+(2*j2)+(2*j3)+j4)
            Py+=(h/6)*(l1+(2*l2)+(2*l3)+l4)

            X.append(Px)
            Y.append(Py)
            T.append(t)
            t+=h

        return T,X,Y



def simulate_motion(T,X,Y):
    fig,ax=plt.subplots()
    ax.set_xlim(min(X)-0.5,max(X)+0.5)
    ax.set_ylim(min(Y)-0.5,max(Y)+0.5)
    ax.set_xlabel("x(t)")
    ax.set_ylabel("y(t)")
    ax.set_title("Van Der Pol Oscillatior Motion")

    point,=ax.plot([],[],"ro")
    trail_lines=[ax.plot([],[],color='blue',alpha=alpha)[0] for alpha in np.linspace(0.1,1,trail_length)]

    def init():
        point.set_data([],[])
        for line in trail_lines: 
            line.set_data([],[])
        return trail_lines+[point]

    
    def update(frame): 
        start=max(0,frame-trail_length)
        for i,line in enumerate(trail_lines):
            idx=start+i
            if idx<len(X):
                line.set_data(X[start:idx+1],Y[start:idx+1])

        point.set_data(X[frame],Y[frame])
        
        return trail_lines+[point]
    ani=animation.FuncAnimation(
        fig,update,frames=len(X),interval=20,blit=True,repeat=True)
    
    plt.show()

def main():
    t=0
    Px0=0
    Py0=0
    Vx0=0.5
    Vy0=0.5

    VDP=VanDerPol(t,Px0,Py0,Vx0,Vy0)
    T,X,Y=VDP.UpdatePositionVelocity()
    simulate_motion(T,X,Y)

  
main()