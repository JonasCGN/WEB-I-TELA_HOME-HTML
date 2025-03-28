const lista = document.getElementById("nav-options")

lista.addEventListener("click",
    (e) => {
        // if(e.detail)
        if(!(e.detail)){
            if(e.target.className != "active"){
                for (let i = 0; i < lista.children.length; i++) {
                    lista.children[i].className = lista.children[i].className.replace("active");
                }
                e.target.className = "active";
            }
        }
    }
)

function verificaPage(){
    const url = window.location.pathname;

    if(url == "/inicio"){
        lista.children[0].className = "active"
    }else if(url == "/contas"){
        lista.children[1].className = "active"
    }else if(url == "/metas"){
        lista.children[2].className = "active"
    }else if(url == "/financas"){
        lista.children[3].className = "active"
    }else if(url == "/historico"){
        lista.children[4].className = "active"
    }else if(url == "/ajuda"){
        lista.children[5].className = "active"
    }else if(url == "/perfil"){
        lista.children[6].className = "active"
    }
}

verificaPage()

function verificaNav(){
    const nav = document.getElementById("list-nav")
    const navigation = document.getElementById("navigation-bar")

    if(navigation.className.search(" occult") < 0){
        nav.src = './assets/list_preto.svg'
        navigation.className += " occult"
    }else{
        nav.src = './assets/list_branco.svg'
        navigation.className = navigation.className.split(" occult")[0]
    }
    // nav.className = "occullt"
}

const profile = document.getElementById("profile-bar")

profile.addEventListener("click",ativaNavigation)

function ativaNavigation(){
    const navigation = document.getElementById("navigation-bar")
    console.log(navigation.className)
    if(navigation.className.search(" activate") < 0){
        navigation.className += " activate"
    }else{
        navigation.className = navigation.className.split(" activate")[0]
    }
}

function getCookie(name) {
    let cookies = document.cookie.split('; ');
    for (let cookie of cookies) {
        let [key, value] = cookie.split('=');
        if (key === name) return decodeURIComponent(value);
    }
    return null;
}

// Atualiza o nome do usuário na tela
let username = getCookie("username"); 
if (username) {
    document.getElementById("username").textContent = username;
}