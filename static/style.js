function toggle_dark_mode() {
    document.body.classList.toggle("dark-mode");

    if (navbar.classList.contains("navbar-light")) {
        navbar.classList.remove("navbar-light");
        navbar.classList.add("navbar-dark");
    } else {
        navbar.classList.remove("navbar-dark");
        navbar.classList.add("navbar-light");
    }
}

/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {
    document.getElementById("sidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";

    let toggle = document.querySelector("#sidebarManager");
    toggle.setAttribute("onclick", "closeNav()");
    toggle.innerHTML = "chevron_left";
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("sidebar").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";

    let toggle = document.querySelector("#sidebarManager");
    toggle.setAttribute("onclick", "openNav()");
    toggle.innerHTML = "settings";
}