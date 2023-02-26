// https://northeast.aaa.com/automotive/registry-services/schedule-rmv.html
// This script is used to get the rmv id and name in the aaa schedule website
function getCalToLocationMap(){
    const list = document.querySelectorAll('#select-calendar-options > div > input')
    const ids = []; 
    list.forEach((node) => { 
        ids.push({
            cal: node.value,
            rmv: node.parentElement.querySelector('#select-calendar-options > div > div.select-label.babel-ignore').innerHTML
        }); 
    })
    console.log(ids)
}

getCalToLocationMap()