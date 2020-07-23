
import pygame
import sys
import json
from bullet import Bullet
from alien import Alien
from time import sleep
from background import Background

#notice that we don't need to define the arguments for the functions we are defining
#however, we have to import methods and classes we want to use and which are not the arguemnts of methods being defined

def check_keydown_events(event, settings, screen, ship, bullets):
    """Respond to keypresses."""
    #easier to test program
    if event.key == pygame.K_q:
        sys.exit()
    #ship movements
    if event.key == pygame.K_RIGHT: #then for event key!
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(settings, screen, ship, bullets):
    """fires bullets - creates a new bullet and add it to the bullets group."""
    if len(bullets) < settings.bullets_allowed: #limiting the number of bullets that can be on the screen
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def check_events(settings, screen, ship, bullets, stats, play_button, aliens, sb):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#watch for keyboard and mouse events.
#an event is an action that the user performs while playing the game, such as pressing a key or moving the mouse.
#To make our program respond to events, we’ll use this for loop to listen for an event and perform
#an appropriate task depending on the kind of event that occurred. 
#To access the events detected by Pygame, we’ll use the pygame.event.get() method. Any keyboard or mouse event will cause the for loop to run.
#Inside the loop, we’ll write a series of if statements to detect and respond to specific events.
#For example, when the player clicks the game window’s close button, a pygame.QUIT event is detected and we call sys.exit() to exit the game

        elif event.type == pygame.KEYDOWN: #notice that first we check for the event.type
            check_keydown_events(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN: #when we click with the mouse
            mouse_x, mouse_y = pygame.mouse.get_pos() #returns a tuple containing the x- and y-coordinates of the mouse cursor when the mouse button is clicked
            check_play_button(settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)


def check_play_button(settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #see if the point of the mouse click overlaps the region defined by the Play button’s rect
        #the flag button_clicked stores a True or False valueu, and the game will restart only if Play is clicked and the game is not currently active

        pygame.mouse.set_visible(False) #hide mouse cursor

        settings.initialize_dynamic_settings() #reset speed settings as we start a new game

        stats.reset_stats() #reset the statistics
        stats.game_active = True

        #empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship.
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        #reset viewed game statistics
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()


def update_screen(settings, screen, stats, ship, aliens, bullets, play_button, sb): 
    """Update images on the screen and flip to the new screen."""
    #screen.fill(settings.bg_color) #fill the screen with a color
    bg = Background('images/bg.jpg', [0,0])
    screen.blit(bg.image, bg.rect)
    sb.show_score()

    for bullet in bullets.sprites(): #bullets.sprites() returns a list of all sprites (items) the bullet list contains so we can loop over them
        bullet.draw_bullet()

    ship.blitme() #draw the ship
    aliens.draw(screen) #draw aliens
    #when you call draw() on a group, Pygame automatically draws each element in the group at the position defined by its rect attribute.
    #In this case, 'aliens.draw(screen)' draws each alien in the group to the screen

    if not stats.game_active: #draw the button if the game is inactive
        play_button.draw_button()

    pygame.display.flip() #make the most recently drawn screen visible, when we move the game elements around,
        #pygame.display.flip() will continually update the display to show the new positions of elements
        #and hide the old ones, creating the illusion of smooth movement


def update_bullets(settings, screen, ship, aliens, bullets, stats, sb):
    """Update position of bullets and get rid of old bullets."""

    bullets.update() #when you call update() on a groupv, the group automatically calls update() for each sprite in the group.
        #The line bullets.update() calls bullet.update() for each bullet we place in the group bullets

    #deleting old bullets
    for bullet in bullets.copy(): #we use copy() method because we cannot alter the list we are looping over
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets, stats, sb)


def check_bullet_alien_collisions(settings, screen, ship, aliens, bullets, stats, sb):
    #check for any bullets that have hit aliens.
    #if so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #the sprite.groupcollide() method compares each bullet’s rect with each alien’s rect and returns a dictionary
    #containing the bullets and aliens that have collided. Each key in the dictionary is a bullet, and the corresponding value is the alien that was hit.
    
    #The two True arguments tell Pygame whether to delete the bullets and aliens that have collided.
    #(To make a high-powered bullet that’s able to travel to the top of the screen, destroying every alien in its path,
    #you could set the first Boolean argument to False and keep the second Boolean argument set to True.
    #The aliens hit would disappear, but all bullets would stay active until they disappeared off the top of the screen.)

    if len(aliens) == 0: #if te current fleet has been all shot down,
        #if the entire fleet is destroyed, start a new level.
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
        #speed up
        settings.increase_speed()

        #increase level by 1
        stats.level += 1
        sb.prep_level()

    if collisions: #if alien has been shot,
        for aliens in collisions.values(): #loop through the values
            stats.score += settings.alien_points * len(aliens) #add points for as many aliens as the list is long
            sb.prep_score() #and render the new image
        check_high_score(stats, sb)

    #any bullet that collides with an alien becomes a key in the collisions dictionary.
    #The value associated with each bullet is a list of aliens it has collided with.
    #We loop through the collisions dictionary to make sure we award points for each alien hit


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    high_score_file = "high_score.json"
    with open(high_score_file) as j_object:
            high_score = json.load(j_object)
    if stats.score > int(high_score):
        with open(high_score_file, 'w') as j_object:
            json.dump(stats.score, j_object)
        sb.prep_high_score()


def get_number_aliens_x(settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (1.9 * alien_width)) #int() cause range function needs integers
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 30
    aliens.add(alien)


def create_fleet(settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    #create an alien and find the number of aliens in a row.
    #Spacing between each alien is equal to one alien width.
    alien = Alien(screen, settings)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)
    
    #create a fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)


def change_fleet_direction(settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def ship_hit(settings, stats, screen, ship, aliens, bullets, sb):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        #decrement ships_left.
        stats.ships_left -= 1

        #update the stats we show
        sb.prep_ships()

        #empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the ship.
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        #pause.
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
            break


def update_aliens(settings, stats, screen, ship, aliens, bullets, sb):
    """Check if the fleet is at an edge and then update the postions of all aliens in the fleet."""
    #because 'aliens' is a Group, calling a method this way will work for all objects in the group
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
    #the method spritecollideany() takes two arguments: a sprite and a group. The method looks for any member of the group
    #that’s collided with the sprite and stops looping through the group as soon as it finds one mem- ber that has collided with the sprite

    #look for aliens hitting the bottom of the screen.
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb)






