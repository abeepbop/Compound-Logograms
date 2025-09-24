import pygame
import numpy as np
import math

class Logogram:
    def __init__(self,identity,center):
        self.ink_color = (117,85,61)
        self.center = center
        self.linewidth = 5
        self.identity = identity
        self.radius = 20
    def draw(self,surface,bg_color):
        elem = self.identity
        radius = self.radius
        self.draw_rec(surface,bg_color,elem,radius,None)

    def draw_rec(self,surface,bg_color,identity,radius,superior_elem):
        last_elem = None
        hollow = True
        for elem in identity:
            if type(elem) is not list:
                if superior_elem is not None:
                    if superior_elem != 0: #or any other hollow shape
                        hollow = False
                
                if elem == 0: # a circle
                    if superior_elem == 0:
                        radius = radius-2*self.linewidth
                    if hollow:
                        pygame.draw.circle(surface,self.ink_color,self.center,radius)
                        pygame.draw.circle(surface,bg_color,self.center,radius-self.linewidth) #Color interior white BEFORE adding more lines
                if elem == 1: # a dot 
                    pygame.draw.circle(surface,self.ink_color,self.center,self.linewidth)
                if elem == 2: # a vertical line
                    start_pos = [self.center[0],self.center[1]-radius]
                    end_pos = [self.center[0],self.center[1]+radius]
                    pygame.draw.line(surface,self.ink_color,start_pos,end_pos,width = self.linewidth)
                if elem == 3: # a horizontal line
                    start_pos = [self.center[0]-radius,self.center[1]]
                    end_pos = [self.center[0]+radius,self.center[1]]
                    pygame.draw.line(surface,self.ink_color,start_pos,end_pos,width = self.linewidth)
                if elem == 4: # an ascending diagonal line
                    start_pos = [self.center[0]-radius,self.center[1]+radius] #TODO fix to be sqrt(2)*radius
                    end_pos   = [self.center[0]+radius,self.center[1]-radius]
                    if superior_elem == 0:
                        start_pos = [self.center[0]-(radius/math.sqrt(2)),self.center[1]+(radius/math.sqrt(2))]
                        end_pos   = [self.center[0]+(radius/math.sqrt(2)),self.center[1]-(radius/math.sqrt(2))]
                    pygame.draw.line(surface,self.ink_color,start_pos,end_pos,width = self.linewidth)
                if elem == 5: # a descending diagonal line
                    start_pos = [self.center[0]-radius,self.center[1]-radius] #TODO fix to be sqrt(2)*radius
                    end_pos = [self.center[0]+radius,self.center[1]+radius]
                    if superior_elem == 0:
                        start_pos = [self.center[0]-(radius/math.sqrt(2)),self.center[1]-(radius/math.sqrt(2))]
                        end_pos   = [self.center[0]+(radius/math.sqrt(2)),self.center[1]+(radius/math.sqrt(2))]
                    pygame.draw.line(surface,self.ink_color,start_pos,end_pos,width = self.linewidth)
                if elem == 6: # an upward half-line
                    end_pos = [self.center[0],self.center[1]-radius]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
                if elem == 7: # a northeast half-line
                    end_pos = [self.center[0]+radius,self.center[1]-radius]
                    if superior_elem == 0:
                        end_pos = [self.center[0]+(radius/math.sqrt(2)),self.center[1]-(radius/math.sqrt(2))]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
                if elem == 8: # an east half-line
                    end_pos = [self.center[0]+radius,self.center[1]]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
                if elem == 9: # a southeast half-line
                    end_pos = [self.center[0]+radius,self.center[1]+radius]
                    if superior_elem == 0:
                        end_pos = [self.center[0]+(radius/math.sqrt(2)),self.center[1]+(radius/math.sqrt(2))]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
                if elem == 10: # a south half-line
                    end_pos = [self.center[0],self.center[1]+radius]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
                if elem == 11: # a southwest half-line
                    end_pos = [self.center[0]-radius,self.center[1]+radius]
                    if superior_elem == 0:
                        end_pos = [self.center[0]-(radius/math.sqrt(2)),self.center[1]+(radius/math.sqrt(2))]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
                if elem == 12: # a west half-line
                    end_pos = [self.center[0]-radius,self.center[1]]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
                if elem == 13: # a northwest half-line
                    end_pos = [self.center[0]-radius,self.center[1]-radius]
                    if superior_elem == 0:
                        end_pos = [self.center[0]-(radius/math.sqrt(2)),self.center[1]-(radius/math.sqrt(2))]
                    pygame.draw.line(surface,self.ink_color,self.center,end_pos,width = self.linewidth)
            else:
                self.draw_rec(surface,bg_color,elem,radius,last_elem)
            if type(elem) is not list:
                last_elem = elem
            last_elem = elem
        