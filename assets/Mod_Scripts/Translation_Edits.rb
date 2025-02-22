class Window_MonsterBook_Info < Window_Base
  def draw_enemy_data(enemy, x, y, opacity = 255)
    fcolor = fc = 0
    #名前
    self.draw_text_enemy_name(x, y, 180, 32, enemy.name, fcolor, 0)
    #レベル
    exceptions = ["Mimic"]
    unless enemy.boss? or exceptions.include?(enemy.name)
      self.draw_text_small(x, y + 50, 300, 32, "Level : ", fc, 0, 2)
      if analyze?(enemy.id)
        self.draw_text_small(x + 75, y + 50, 300, 32, enemy.level.to_s, fc, 0, 2)
      else
        self.draw_text_small(x + 75, y + 50, 300, 32, "？", fc, 0, 2)
      end
    end
    #性格
    self.draw_text_small(x, y+50+25, 300, 32, "Personality: ", fc, 0, 2)
    if analyze?(enemy.id)
      self.draw_text_small(x+75, y+50+25, 300, 32, enemy.description(1), fc, 0, 2)
    else
      self.draw_text_small(x+75, y+50+25, 300, 32, "？", fc, 0, 2)
    end
    #弱点
    self.draw_text_small(x, y+50+50, 300, 32, "Weakness: ", fc, 0, 2)
    if analyze?(enemy.id)
      self.draw_text_small(x+75, y+50+50, 300, 32, enemy.description(2), fc, 0, 2)
    else
      self.draw_text_small(x+75, y+50+50, 300, 32, "？", fc, 0, 2)
    end
    #出典
    self.draw_text_small(x, y+155, 300, 32, "Origin: ", fc, 0, 2)
    self.draw_text_small(x+42, y+155, 300, 32, enemy.comment(0), fc, 0, 2)
    #コメント
    self.draw_text_small(x, y + 165+25, 320, 32, enemy.comment(1), fc, 0, 2)
    self.draw_text_small(x, y + 165+50, 320, 32, enemy.comment(2), fc, 0, 2)
    self.draw_text_small(x, y + 165+75, 320, 32, enemy.comment(3), fc, 0, 2)
    self.draw_text_small(x, y + 165+100, 320, 32, enemy.comment(4), fc, 0, 2)
    self.draw_text_small(x, y + 165+125, 320, 32, enemy.comment(5), fc, 0, 2)
    self.draw_text_small(x, y + 165+150, 320, 32, enemy.comment(6), fc, 0, 2)
    self.draw_text_small(x, y + 165+175, 320, 32, enemy.comment(7), fc, 0, 2)
    self.draw_text_small(x, y + 165+200, 320, 32, enemy.comment(8), fc, 0, 2)
    self.draw_text_small(x, y + 165+225, 320, 32, enemy.comment(9), fc, 0, 2)
    self.draw_text_small(x, y + 165+250, 320, 32, enemy.comment(10), fc, 0, 2)
  end
end