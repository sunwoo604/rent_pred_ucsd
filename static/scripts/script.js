function update_val(id){
    var inp =  document.getElementById(id)
    if (id === 'bedSlider'){
        var o = document.getElementById('currBed');
    }
    else{
        var o = document.getElementById('currBath');
    }
    o.innerHTML = o.innerHTML.substring(0, o.innerHTML.length - 1) + inp.value
}

function get_prediction(){
    var xhr = new XMLHttpRequest();
    //setting the function to be called when there is a status change in request
    //(which means there is a return value from the server)
    xhr.onreadystatechange = function(){
        var response = xhr.responseText;
        update_result(response)

    }
    xhr.open('POST', '/prediction');
    var city = document.getElementById('city-dropdown')
    city = city.options[city.selectedIndex].value;
    var post_var = {
        'bed': document.getElementById('bedSlider').value,
        'bath': document.getElementById('bathSlider').value,
        'city': city
    }
    post_var = formulate_post_string(post_var)
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send(post_var);
}

function formulate_post_string(dict){
    var out =""
    for (const key in dict) {
        if (out.length != 0){
            out+="&"
        }
        out+=key
        out+="="
        out+=dict[key]
    }
    return out
}

function update_result(val){
    var o = document.getElementById('result-text')
    o.innerHTML = 'Based on the given values, our model predicted the rent to be around '+val
}