function sortSelectorFunction() {
    var selector = document.getElementById("sort-selector").value;
    var currentUrl = new URL(window.location)

    if(selector != 'reset') {
        var sort = selector.split("_")[0]
        var direction = selector.split("_")[1]

        currentUrl.searchParams.set("sort", sort)
        currentUrl.searchParams.set("direction", direction)

        window.location.replace(currentUrl)
    } else {
        currentUrl.searchParams.delete("sort")
        currentUrl.searchParams.delete("direction")

        window.location.replace(currentUrl)
    }
}

var btnBackTop = document.getElementById('btt-back-top')
btnBackTop.addEventListener('click', () => {
    window.scrollTo(0,0)
})