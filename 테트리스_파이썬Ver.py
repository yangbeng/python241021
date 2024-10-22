import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

# 게임 설정
CELL_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# 테트로미노 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.randint(1, len(COLORS) - 1)
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("테트리스")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetromino()
        self.game_over = False
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.drop_speed = 0.5
        self.fast_drop = False

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(self.screen, COLORS[self.grid[y][x]],
                                 (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)

    def draw_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[self.current_piece.color],
                                     ((self.current_piece.x + x) * CELL_SIZE,
                                      (self.current_piece.y + y) * CELL_SIZE,
                                      CELL_SIZE, CELL_SIZE), 0)

    def move(self, dx, dy):
        if self.valid_move(self.current_piece.x + dx, self.current_piece.y + dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
            return True
        return False

    def valid_move(self, x, y):
        for y_offset, row in enumerate(self.current_piece.shape):
            for x_offset, cell in enumerate(row):
                if cell:
                    if (x + x_offset < 0 or x + x_offset >= GRID_WIDTH or
                        y + y_offset >= GRID_HEIGHT or
                        self.grid[y + y_offset][x + x_offset]):
                        return False
        return True

    def rotate_piece(self):
        original_shape = self.current_piece.shape
        self.current_piece.rotate()
        if not self.valid_move(self.current_piece.x, self.current_piece.y):
            self.current_piece.shape = original_shape

    def merge_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color
        self.clear_lines()
        self.current_piece = Tetromino()
        if not self.valid_move(self.current_piece.x, self.current_piece.y):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT - 1, -1, -1):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared ** 2 * 100

    def run(self):
        fall_time = 0
        while not self.game_over:
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1, 0)
                    if event.key == pygame.K_RIGHT:
                        self.move(1, 0)
                    if event.key == pygame.K_DOWN:
                        self.move(0, 1)
                    if event.key == pygame.K_UP:
                        self.rotate_piece()
                    if event.key == pygame.K_SPACE:
                        self.fast_drop = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.fast_drop = False

            current_speed = 0.05 if self.fast_drop else self.drop_speed
            if fall_time / 1000 > current_speed:
                if not self.move(0, 1):
                    self.merge_piece()
                fall_time = 0

            self.screen.fill(BLACK)
            self.draw_grid()
            self.draw_piece()
            score_text = self.font.render(f"점수: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()