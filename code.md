       if not keys[Pg.K_a] and not keys[Pg.K_d]:
            self.speed_X = 0
            self.player = self.rect[0]                                       # Standart
        if not keys[Pg.K_w] and not keys[Pg.K_s]:
            self.speed_Y = 0
            self.player = self.rect[0]                                      # Standart
        if keys[Pg.K_z]:
            for BULLET in range(keys[Pg.K_z]):
                self.speed_bullet_y = -10








    # Diseño
    # for coord in coor_list:
    #     x = coord[0]
    #     y = coord[1]
    #     pygame.draw.circle(Ventana, White, (x,y), 4)
    #     coord[1] += 1
    #     if coord[1] > alto:
    #         coord[1] = 0
    # for coord1 in coor_list1:
    #     x = coord1[0]
    #     y = coord1[1]
    #     pygame.draw.circle(Ventana, White, (x,y), 4)
    #     coord1[0] += 1
    #     if coord1[0] > 572:
    #         coord1[0] = 225