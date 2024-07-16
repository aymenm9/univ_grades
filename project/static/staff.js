
function checkViewport(){
    const offcanvas = document.getElementById("staffOffcanvas");
    if (window.innerWidth < 768) {
        offcanvas.classList.remove('show', 'w-25');
        offcanvas.classList.add('w-75');
    } else {
        offcanvas.classList.add('show', 'w-25');
        offcanvas.classList.remove('w-75');
        console.log('test2');
    }
    console.log('test');
}

document.addEventListener("DOMContentLoaded", checkViewport);

window.addEventListener('resize', function () { 
    console.log('test3');
    checkViewport(); });

