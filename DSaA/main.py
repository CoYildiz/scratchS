from manim import *
from linked_list2 import LinkedList 

class DynamicLinkedList(Scene):
    def construct(self):


        my_list = LinkedList(10, 20, 30, 40)
        
  
        title = Text("Dinamik Linked List", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Görsel düğüm oluşturan yardımcı fonksiyon
        def create_visual_node(value, position):
            box = Square(side_length=1, color=BLUE)
            text = Text(str(value), font_size=36)
            return VGroup(box, text).move_to(position)

        # döngü değişkenleri
        current_logical_node = my_list._head # sinifdaki _head
        start_x = -5 # Ekranın solundan çizmeye başlamak için
        prev_visual_node = None 


        while current_logical_node is not None:
            
            # o anki düğümün görselini oluştur
            pos = RIGHT * start_x
            current_visual_node = create_visual_node(current_logical_node.value, pos)
            

            self.play(Create(current_visual_node), run_time=0.5)
            

            if prev_visual_node is not None:
                pointer = Arrow(
                    start=prev_visual_node.get_right(), 
                    end=current_visual_node.get_left(), 
                    buff=0.1, color=YELLOW
                )
                self.play(GrowArrow(pointer), run_time=0.4)
            

            prev_visual_node = current_visual_node
            current_logical_node = current_logical_node.next 
            start_x += 2.5 # bir sonraki node u kaydır
            
        self.wait(2)
