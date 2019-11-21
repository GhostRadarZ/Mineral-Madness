import pygame, entity, hitbox

#
# Characters
# Contains specific character balancing, and information
#

class Pebble(entity.Character):
    def __init__(self, lives, spawnpos):
        # Inherit from the Entity class
        super(Pebble, self).__init__(lives, spawnpos)

        # Hurtbox dimensions
        self.hurtbox.width = 60
        self.hurtbox.height = 72

        # Set the inital coordinates of the character
        self.x = self.spawnpos[0] - self.hurtbox.width / 2
        self.y = self.spawnpos[1] - self.hurtbox.height

        # Movement speed in x-direction
        self.x_base = 10

        # Initial jump speed
        self.y_base = 15

        # Fast fall speed
        self.y_base_fast = 20

        # Gravity constant
        self.gravity = 1

        # Grounded forward attack frame data for Pebble
        self.atkforward_attack = [
            [
                [hitbox.Melee, (pygame.Rect(26, 32, 28, 24), 5, 5, 8, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(34, 28, 28, 24), 5, 5, 8, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(42, 20, 36, 36), 5, 5, 8, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(38, 8, 52, 56), 5, 5, 8, 20)],
                [hitbox.Projectile, (54, 32, 10, 0, 0, 2, 2, 6, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(34, 4, 60, 64), 5, 5, 8, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 0, 72, 68), 5, 5, 8, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 0, 72, 68), 5, 5, 8, 20)]
            ]
        ]

        # Aerial forward attack frame data for Pebble
        self.aerialforward_attack = [
            [
                [hitbox.Melee, (pygame.Rect(24, 16, 20, 16), 3, 2, 4, 15)],
                [hitbox.Melee, (pygame.Rect(-44, 16, 20, 16), -3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(24, 12, 28, 24), 3, 2, 4, 15)],
                [hitbox.Melee, (pygame.Rect(-52, 12, 28, 24), -3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(28, 8, 32, 32), 3, 2, 4, 15)],
                [hitbox.Melee, (pygame.Rect(-60, 8, 32, 32), -3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(32, 4, 36, 36), 3, 2, 4, 15)],
                [hitbox.Melee, (pygame.Rect(-68, 4, 36, 36), -3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(36, 4, 36, 36), 3, 2, 4, 15)],
                [hitbox.Melee, (pygame.Rect(-72, 4, 36, 36), -3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(40, 4, 36, 36), 3, 2, 4, 15)],
                [hitbox.Melee, (pygame.Rect(-76, 4, 36, 36), -3, 2, 4, 15)]
            ]
        ]

        # Grounded up attack frame data for Pebble
        self.atkup_attack = [
            [
                [hitbox.Melee, (pygame.Rect(-30, -4, 60, 16), 1, 6, 6, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-30, -12, 60, 16), 1, 6, 6, 15)]
            ]
        ]

        # Aerial up attack frame data for Pebble
        self.aerialup_attack = [
            [
                [hitbox.Melee, (pygame.Rect(-12, -24, 32, 40), 2, 6, 6, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-12, -24, 32, 40), 2, 6, 6, 30)]
            ]
        ]

        # Grounded down attack frame data for Pebble
        self.atkdown_attack = [
            [
                [[None]]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 56, 24, 16), 1, 3, 2, 5)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 56, 24, 16), 1, 5, 4, 8)],
                [hitbox.Melee, (pygame.Rect(62, 56, 44, 16), 1, 5, 4, 8)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 56, 24, 16), 2, 7, 6, 10)],
                [hitbox.Melee, (pygame.Rect(62, 44, 44, 28), 2, 7, 6, 10)],
                [hitbox.Melee, (pygame.Rect(114, 20, 80, 52), 2, 7, 6, 10)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 56, 24, 16), 2, 7, 8, 12)],
                [hitbox.Melee, (pygame.Rect(62, 40, 44, 32), 2, 7, 8, 12)],
                [hitbox.Melee, (pygame.Rect(114, -4, 80, 76), 2, 7, 8, 12)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 52, 24, 20), 2, 9, 10, 15)],
                [hitbox.Melee, (pygame.Rect(62, 32, 44, 40), 2, 9, 10, 15)],
                [hitbox.Melee, (pygame.Rect(114, -16, 80, 88), 2, 9, 10, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 48, 24, 24), 2, 9, 10, 15)],
                [hitbox.Melee, (pygame.Rect(62, 24, 44, 48), 2, 9, 10, 15)],
                [hitbox.Melee, (pygame.Rect(114, -28, 80, 100), 2, 9, 10, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(30, 44, 24, 28), 2, 9, 10, 15)],
                [hitbox.Melee, (pygame.Rect(62, 16, 44, 56), 2, 9, 10, 15)],
                [hitbox.Melee, (pygame.Rect(114, -40, 80, 112), 2, 9, 10, 15)]
            ]
        ]

        # Aerial down attack frame data for Pebble
        self.aerialdown_attack = [
            [
                [hitbox.Melee, (pygame.Rect(-18, 32, 36, 40), 2, -6, 10, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-18, 32, 36, 40), 2, -6, 10, 30)]
            ]
        ]

class Crystal(entity.Character):
    def __init__(self, lives, spawnpos):
        # Inherit from the Entity class
        super(Crystal, self).__init__(lives, spawnpos)

        # Hurtbox dimensions
        self.hurtbox.width = 56
        self.hurtbox.height = 84

        # Set the inital coordinates of the character
        self.x = self.spawnpos[0] - self.hurtbox.width / 2
        self.y = self.spawnpos[1] - self.hurtbox.height

        # Movement speed in x-direction
        self.x_base = 8

        # Initial jump speed
        self.y_base = 13

        # Fast fall speed
        self.y_base_fast = 17

        # Gravity constant
        self.gravity = 0.7

        # Grounded forward attack frame data for Crystal
        self.atkforward_attack = [
            [
                [hitbox.Melee, (pygame.Rect(16, 44, 56, 16), 2, 2, 5, 10)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(32, 44, 56, 16), 2, 2, 5, 10)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(40, 44, 56, 16), 2, 2, 5, 10)]
            ]
        ]

        # Aerial forward attack frame data for Crystal
        self.aerialforward_attack = [
            [
                [hitbox.Melee, (pygame.Rect(12, -36, 16, 56), 2, 2, 6, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(32, -36, 40, 64), 2, 2, 6, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(32, -20, 56, 104), 2, 2, 6, 20)]
            ]
        ]

        # Grounded up attack frame data for Crystal
        self.atkup_attack = [
            [
                [hitbox.Melee, (pygame.Rect(20, -36, 40, 44), 1, 5, 9, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-8, -68, 64, 60), 1, 5, 9, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-60, -68, 76, 76), 1, 5, 9, 20)]
            ]
        ]

        # Aerial up attack frame data for Crystal
        self.aerialup_attack = [
            [
                [hitbox.Melee, (pygame.Rect(16, -36, 52, 60), 1, 6, 7, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-4, -60, 56, 56), 1, 6, 7, 20)]
            ]
        ]

        # Grounded down attack frame data for Crystal
        self.atkdown_attack = [
            [
                [hitbox.Melee, (pygame.Rect(16, 68, 52, 16), 5, 1, 5, 10)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(40, 68, 52, 16), 5, 1, 5, 10)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(48, 68, 52, 16), 5, 1, 5, 10)]
            ]
        ]

        # Aerial down attack frame data for Crystal
        self.aerialdown_attack = [
            [
                [hitbox.Melee, (pygame.Rect(20, 12, 52, 72), 2, -6, 10, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(4, 56, 44, 68), 2, -6, 10, 20)]
            ]
        ]

class Magma(entity.Character):
    def __init__(self, lives, spawnpos):
        # Inherit from the Entity class
        super(Magma, self).__init__(lives, spawnpos)

        # Hurtbox Dimensions
        self.hurtbox.width = 76
        self.hurtbox.height = 108

        # Set the inital coordinates of the character
        self.x = self.spawnpos[0] - self.hurtbox.width / 2
        self.y = self.spawnpos[1] - self.hurtbox.height

        # Movement speed in x-direction
        self.x_base = 5

        # Initial jump speed
        self.y_base = 10

        # Fast fall speed
        self.y_base_fast = 15

        # Gravity constant
        self.gravity = 0.5

        # Grounded forward attack frame data for Magma
        self.atkforward_attack = [
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [hitbox.Projectile, (38, 24, 10, 0, 0, 2, 2, 6, 18)]
            ]
        ]

        # Aerial forward attack frame data for Magma
        self.aerialforward_attack = [
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [hitbox.Projectile, (38, 24, 10, 0, 0, 2, 2, 6, 18)]
            ]
        ]

        # Grounded up attack frame data for Magma
        self.atkup_attack = [
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-30, -12, 60, 60), 1, 9, 15, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-42, -24, 84, 72), 1, 9, 15, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-42, -12, 88, 76), 1, 9, 15, 30)]
            ]
        ]

        # Aerial up attack frame data for Magma
        self.aerialup_attack = [
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-70, 24, 28, 56), 5, 2, 7, 25)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-70, 112, 88, 28), 5, 2, 7, 25)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(42, 48, 28, 92), 5, 2, 7, 25)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-18, 12, 88, 36), 5, 2, 7, 25)]
            ]
        ]

        # Grounded down attack frame data for Magma
        self.atkdown_attack = [
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(38, 80, 40, 28), 5, 2, 20, 25)],
                [hitbox.Melee, (pygame.Rect(-78, 80, 40, 28), -5, 2, 20, 25)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(38, 60, 56, 48), 5, 2, 20, 25)],
                [hitbox.Melee, (pygame.Rect(-94, 60, 56, 48), -5, 2, 20, 25)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(38, 56, 60, 52), 5, 2, 20, 25)],
                [hitbox.Melee, (pygame.Rect(-98, 56, 60, 52), -5, 2, 20, 25)]
            ]
        ]

        # Aerial down attack frame data for Magma
        self.aerialdown_attack = [
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-22, 108, 44, 20), 2, -9, 15, 25)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-38, 108, 76, 36), 2, -9, 15, 25)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-38, 108, 76, 36), 2, -9, 15, 25)]
            ]
        ]

class Pharaoh(entity.Character):
    def __init__(self, lives, spawnpos):
        # Inherit from the Entity class
        super(Pharaoh, self).__init__(lives, spawnpos)

        # Hurtbox Dimensions
        self.hurtbox.width = 36
        self.hurtbox.height = 80

        # Set the inital coordinates of the character
        self.x = self.spawnpos[0] - self.hurtbox.width / 2
        self.y = self.spawnpos[1] - self.hurtbox.height

        # Movement speed in x-direction
        self.x_base = 8

        # Initial jump speed
        self.y_base = 14

        # Fast fall speed
        self.y_base_fast = 20

        # Gravity constant
        self.gravity = 0.8

        # Grounded forward attack frame data for Pharaoh
        self.atkforward_attack = [
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [hitbox.Projectile, (26, 16, 10, -2, 1, 2, 0, 3, 5)],
                [hitbox.Projectile, (26, 16, 10, -6, 1, 2, 0, 3, 5)],
                [hitbox.Projectile, (26, 16, 10, -8, 1, 2, 0, 3, 5)]
            ]
        ]

        # Aerial forward attack frame data for Pharaoh
        self.aerialforward_attack = [
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(22, 28, 8, 16), 3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(22, 28, 16, 16), 3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(22, 28, 24, 16), 3, 2, 4, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(22, 28, 28, 16), 3, 2, 4, 15)],
                [hitbox.Projectile, (26, 16, 10, -2, 1, 2, 0, 3, 5)],
                [hitbox.Projectile, (26, 16, 10, -6, 1, 2, 0, 3, 5)],
                [hitbox.Projectile, (26, 16, 10, -8, 1, 2, 0, 3, 5)]
            ]
        ]

        # Grounded up attack frame data for Pharaoh
        self.atkup_attack = [
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(26, 28, 20, 52), 1, 8, 6, 20)],
                [hitbox.Melee, (pygame.Rect(-46, 28, 20, 52), -1, 8, 6, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(26, 0, 20, 80), 1, 8, 6, 20)],
                [hitbox.Melee, (pygame.Rect(-46, 0, 20, 80), -1, 8, 6, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(26, -28, 20, 108), 1, 8, 6, 20)],
                [hitbox.Melee, (pygame.Rect(-46, -24, 20, 104), -1, 8, 6, 20)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(26, -56, 20, 136), 1, 8, 6, 20)],
                [hitbox.Melee, (pygame.Rect(-46, -56, 20, 136), -1, 8, 6, 20)]
            ]
        ]

        # Aerial up attack frame data for Pharaoh
        self.aerialup_attack = [
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(10, 20, 12, 12), 1, 6, 6, 30)],
                [hitbox.Melee, (pygame.Rect(-22, 20, 12, 12), -1, 6, 6, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(10, 12, 20, 20), 1, 6, 6, 30)],
                [hitbox.Melee, (pygame.Rect(-30, 12, 20, 20), -1, 6, 6, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(10, 8, 24, 24), 1, 6, 6, 30)],
                [hitbox.Melee, (pygame.Rect(-34, 8, 24, 24), -1, 6, 6, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(10, 4, 28, 28), 1, 6, 6, 30)],
                [hitbox.Melee, (pygame.Rect(-38, 4, 28, 28), -1, 6, 6, 30)],
                [hitbox.Projectile, (0, 0, 0, -6, 1, 2, 0, 3, 5)],
                [hitbox.Projectile, (10, 4, 7, -3, 1, 2, 0, 3, 5)],
                [hitbox.Projectile, (-38, 4, -7, -3, 1, 2, 0, 3, 5)]
            ]
        ]

        # Grounded down attack frame data for Pharaoh
        self.atkdown_attack = [
            [
                [hitbox.Melee, (pygame.Rect(-32, 64, 52, 16), 6, 1, 8, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-24, 64, 44, 16), 6, 1, 8, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-16, 64, 36, 16), 6, 1, 8, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-16, 64, 32, 16), 6, 1, 8, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-16, 64, 44, 16), 6, 1, 8, 15)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-16, 64, 52, 16), 6, 1, 8, 15)]
            ]
        ]

        # Aerial down attack frame data for Pharaoh
        self.aerialdown_attack = [
            [
                [None]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-10, 72, 20, 16), 2, -6, 10, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-10, 72, 20, 24), 2, -6, 10, 30)]
            ],
            [
                [hitbox.Melee, (pygame.Rect(-10, 72, 20, 28), 2, -6, 10, 30)]
            ]
        ]
