
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    player1.move('right')
  elif keys[pygame.K_LEFT]:
    player1.move('left')
  if keys[pygame.K_UP]:
    player1.move('up')
  elif keys[pygame.K_DOWN]:
    player1.move('down')

  if keys[pygame.K_d]:
    player2.move('right')
  elif keys[pygame.K_a]:
    player2.move('left')
  if keys[pygame.K_w]:
    player2.move('up')
  elif keys[pygame.K_s]:
    player2.move('down')
