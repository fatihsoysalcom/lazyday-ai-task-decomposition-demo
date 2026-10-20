import time
import random

def lazyday_ai_breakdown(task_name, complexity_score):
    """
    Simulates the LazyDay AI's approach to breaking down a large task
    into smaller, manageable "micro-tasks" based on perceived complexity.
    This is where the 'AI' (systematic approach) helps reduce overthinking.
    """
    print(f"\nLazyDay AI: '{task_name}' görevini analiz ediyor...")
    time.sleep(1)

    micro_tasks = []
    # The 'AI' logic: More complex tasks are broken into more micro-tasks.
    # This systematic breakdown helps combat overthinking and procrastination.
    num_micro_tasks = max(3, complexity_score * 2) 
    
    for i in range(num_micro_tasks):
        # Generate a small, actionable micro-task description
        action_verbs = ["Araştır", "Taslağı Oluştur", "Not Al", "Planla", "İlk Adımı At", "Kontrol Et"]
        specific_details = [
            "giriş bölümünü", "ana hatları", "kaynakları", "örnekleri",
            "ilk paragrafı", "gerekli araçları", "hedef kitleyi", "anahtar kelimeleri"
        ]
        micro_task_desc = f"{random.choice(action_verbs)} {random.choice(specific_details)} ({i+1}/{num_micro_tasks})"
        micro_tasks.append(micro_task_desc)
    
    print(f"LazyDay AI: '{task_name}' görevi {len(micro_tasks)} küçük adıma bölündü.")
    return micro_tasks

def lazyday_ai_progress(project_goal, major_tasks):
    """
    Simulates working through a project using the LazyDay AI philosophy.
    Focuses on completing small, manageable steps and celebrating progress.
    """
    print(f"\n--- LazyDay AI ile Proje Başlangıcı: '{project_goal}' ---")
    total_micro_tasks_completed = 0

    for i, (task_name, complexity) in enumerate(major_tasks):
        print(f"\n[{i+1}/{len(major_tasks)}] Ana Görev: '{task_name}' (Karmaşıklık: {complexity}/5)")
        micro_tasks = lazyday_ai_breakdown(task_name, complexity)
        
        for j, micro_task in enumerate(micro_tasks):
            print(f"  -> Küçük Adım: '{micro_task}'")
            # Simulate a small amount of work/delay for each micro-task
            time.sleep(random.uniform(0.1, 0.5)) 
            print(f"     [TAMAMLANDI] '{micro_task}'")
            total_micro_tasks_completed += 1
            # Celebrate small success, reinforcing the LazyDay AI principle
            if (j + 1) % 3 == 0 or (j + 1) == len(micro_tasks):
                print(f"     LazyDay AI: Harika! {total_micro_tasks_completed} küçük adım tamamlandı bile. Devam edin!")
            
    print(f"\n--- Proje Sonucu: '{project_goal}' ---")
    print(f"Toplamda {total_micro_tasks_completed} küçük adım tamamlanarak proje ilerletildi.")
    print("LazyDay AI: Aşırı düşünmeyi bıraktınız ve küçük adımlarla büyük bir yol kat ettiniz. Tebrikler!")

if __name__ == "__main__":
    # Example Project Definition: A daunting task broken into major components
    project_goal = "Yeni Bir Blog Yazısı Yazmak"
    major_tasks = [
        ("Konu Araştırması Yapmak", 3),
        ("Ana Hatları Oluşturmak", 4),
        ("İlk Taslağı Yazmak", 5),
        ("Görselleri Seçmek ve Eklemek", 2),
        ("Yazıyı Gözden Geçirmek ve Düzenlemek", 4),
        ("Yayınlamak", 1)
    ]

    lazyday_ai_progress(project_goal, major_tasks)
