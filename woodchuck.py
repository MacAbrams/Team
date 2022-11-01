




class woodChuckBrain:

  def wood_per_chuck():
    while 1:
      wood = input("How much wood?: ")
      if wood.replace(".", "").isdigit():
        wood = float(wood)
        break
    while 1:
      chucks = input("How many chucks?: ")
      if chucks.replace(".", "").isdigit():
        chucks = float(chucks)
        break
      
    return f"Your chucks are chucking {wood / chucks} wood per chuck."


  def chuck_speed():
    
    while 1:
      chucks = input("How many chucks?: ")
      if chucks.replace(".", "").isdigit():
        chucks = float(chucks)
        break

    while 1:
      seconds = input("How many seconds?: ")
      if seconds.replace(".", "").isdigit():
        seconds = float(seconds)
        break

    return f"Your chucks are chucking at a speed of {chucks / seconds} chucks per second."


  def wood_per_second():

    while 1:
      wood = input("How much wood?: ")
      if wood.replace(".", "").isdigit():
        wood = float(wood)
        break
    
    while 1:
      seconds = input("How many seconds?: ")
      if seconds.replace(".", "").isdigit():
        seconds = float(seconds)
        break
      
    return f"Your chucks are chucking {wood / seconds} wood per second."

  def strength_of_chucks():
    while 1:
      wood = input("How much wood?: ")
      if wood.replace(".", "").isdigit():
        wood = float(wood)
        break
        
    while 1:
      chucks = input("How many chucks?: ")
      if chucks.replace(".", "").isdigit():
        chucks = float(chucks)
        break

    if wood/chucks >= 10:
      return f"Your chucks are very strong with {wood/chucks} wood per chuck."
    elif wood/chucks < 10:
      return f"Your chucks are very weak with a measly {wood/chucks} wood per chuck."
    
    
     
