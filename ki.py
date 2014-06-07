import pygame
import socket 

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
a=[0,0]
b=[0,0,0,0,0,0,0,0,0,0,0]
s = socket.socket()         # Create a socket object
host = '192.168.0.101'             # Get local machine name
port = 8080                 # Reserve a port for your service.
s.bind((host, port)) 
s.listen(5)   
# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputing the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printa(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while True:
   c, addr = s.accept()     # Establish connection with client.
   
   
     
   while done==False:
    # EVENT PROCESSING STEP
       for event in pygame.event.get(): # User did something
           if event.type == pygame.QUIT: # If user clicked close
               done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
           if event.type == pygame.JOYBUTTONDOWN:
               print("Joystick button pressed.")
           if event.type == pygame.JOYBUTTONUP:
               print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
           screen.fill(WHITE)
  	   textPrint.reset()

    # Get count of joysticks
           joystick_count = pygame.joystick.get_count()

           textPrint.printa(screen, "Number of joysticks: {}".format(joystick_count) )
	   textPrint.indent()
    
    	# For each joystick:
   	   for i in range(joystick_count):
   	        joystick = pygame.joystick.Joystick(i)
  	        joystick.init()
    
                textPrint.printa(screen, "Joystick {}".format(i) )
                textPrint.indent()
    
        	# Get the name from the OS for the controller/joystick
           	name = joystick.get_name()
             	textPrint.printa(screen, "Joystick name: {}".format(name) )
        
        	# Usually axis run in pairs, up/down for one, and left/right for
        	# the other.
        	axes = joystick.get_numaxes()
        	textPrint.printa(screen, "Number of axes: {}".format(axes) )
        	textPrint.indent()
        	
        	for i in range( axes ):
        	    axis = joystick.get_axis( i )
        	    textPrint.printa(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
        	    a[i]=axis
		    if a[1]==-1:
        	      c.send('u')
        	    if a[0]==-1:
		      c.send('l')
		    if a[1]>0:
		      c.send('d')
		    if a[0]>0:
		      c.send('r')
		    if b[0]==1:
			c.send('hu')
                    if b[1]==1:
                        c.send('hd')
                    if b[2]==1:
                        c.send('hold')
                    if b[3]==1:
                        c.send('lea')
                    if b[4]==1:
                        c.send('su')
                    if b[6]==1:
                        c.send('sd')
		    if b[5]==1:
			c.send('stop')
		    if b[9]==1:
			c.send('ping1')
		    if b[8]==1:
			c.send('cd')
		    if b[7]==1:
			c.send('cl')
	        textPrint.unindent()
            
	        buttons = joystick.get_numbuttons()
	        textPrint.printa(screen, "Number of buttons: {}".format(buttons) )
	        textPrint.indent()

        	for i in range( buttons ):
        	    button = joystick.get_button( i )
        	    textPrint.printa(screen, "Button {:>2} value: {}".format(i,button) )
        	    b[i]=button
		    if b[i]!=0:
			print "pressed"
    	        textPrint.unindent()
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
    	        hats = joystick.get_numhats()
    	        textPrint.printa(screen, "Number of hats: {}".format(hats) )
    	        textPrint.indent()

     	        for i in range( hats ):
	            hat = joystick.get_hat( i )
 	            textPrint.printa(screen, "Hat {} value: {}".format(i, str(hat)) )
    	        textPrint.unindent()
        
  	        textPrint.unindent()

    
  	  # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
  	  
  	  # Go ahead and update the screen with what we've drawn.
  	        pygame.display.flip()

  	  # Limit to 20 frames per second
       clock.tick(20)
   c.close() 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()

