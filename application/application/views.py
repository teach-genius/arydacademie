from django.shortcuts import render



def home_view(request):
    a = [
        {   "icon":"fa-solid fa-people-group",
            "title":"Apprentissage Collectif",
            "description":"Progressez ensemble dans une communauté soudée d'apprenants et de mentors."
        },
        {   "icon":"fa-solid fa-code",
            "title":"Projets Pratiques",
            "description":"Apprenez en réalisant des projets concrets guidés par des experts."
        },
        {   "icon":"fa-solid fa-book-open",
            "title":"Ressources Spécialisées",
            "description":"Accédez à des contenus de qualité en développement et technologies."
        },
        {
            "icon":"fa-solid fa-brain",
            "title":"Mentorat Personnalisé",
            "description":"Bénéficiez d'un suivi individuel par des professionnels expérimentés."
        }
    ]
    programmes = [
        {
        "url":"https://img.freepik.com/free-photo/programming-background-collage_23-2149901783.jpg?uid=R98303208&ga=GA1.1.1436796844.1740961606&semt=ais_hybrid",
        "title":"Développement Web",
        "description":"Frontend & Backend"
        }
        ,
        {
        "url":"https://img.freepik.com/free-photo/saas-concept-collage_23-2149399284.jpg?uid=R98303208&ga=GA1.1.1436796844.1740961606&semt=ais_hybrid",
        "title":"DevOps & Cloud",
        "description":"Infrastructure & CI/CD"
        }
        ,
        {
        "url":"https://img.freepik.com/free-vector/ai-technology-microchip-background-vector-digital-transformation-concept_53876-112222.jpg?uid=R98303208&ga=GA1.1.1436796844.1740961606&semt=ais_hybrid",
        "title":"Intelligence Artificielle",
        "description":"ML & Deep Learning"
        }
        ,
        {
        "url":"https://img.freepik.com/free-vector/3d-earth-graphic-symbolizing-global-trade-illustration_456031-125.jpg?uid=R98303208&ga=GA1.1.1436796844.1740961606&semt=ais_hybrid",
        "title":"Réseau",
        "description":"Adressage & Routage"
        }
        ,
        {
        "url":"https://img.freepik.com/free-photo/man-holding-smartphone-with-apartment-buildings-hologram_23-2149369107.jpg?uid=R98303208&ga=GA1.1.1436796844.1740961606&semt=ais_hybrid",
        "title":"Architecture Logicielle",
        "description":"Design Patterns & Best Practices"
        }
        ,
        {
        "url":"https://img.freepik.com/free-photo/smartphone-with-user-interface-concept_52683-104212.jpg?uid=R98303208&ga=GA1.1.1436796844.1740961606&semt=ais_hybrid",
        "title": "Mobile & Apps",
        "description": "Cross-Platform"
        }
        
    ]
    comments = [
        {
            "text":"EduLearn completely transformed my career. The courses were comprehensive and the instructors were incredibly knowledgeable.",
            "name":"Sarah Johnson",
            "fonction":"Software Developer",
            "profile":"https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
            "stars":[i for i in range(5)]
        },
        {
            "text":"I've tried many online learning platforms, but EduLearn stands out with its interactive approach and supportive community.",
            "name":"Michael Chen",
            "fonction":"Marketing Specialist",
            "profile":"https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
            "stars":[i for i in range(5)]
        }
        ,
        {
            "text":"The flexibility of learning at my own pace while still having access to expert guidance made all the difference in my learning journey.",
            "name":"Jessica Williams",
            "fonction":"Data Scientist",
            "profile":"https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
            "stars":[i for i in range(5)]
        }
    ]
    context = {"options":a,"comments":comments,"programmes":zip(programmes,range(len(programmes)))}
    return render(request,"index.html",context)