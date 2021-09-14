var i = 0;

function duplicate() {
    if(i < 9){
        document.getElementById('addform').onclick = duplicate;
        var original = document.getElementById('uploadfile0');
        var clone = original.cloneNode();
        i += 1;
        clone.setAttribute('name','uploadfile' + i);
        clone.setAttribute('id','uploadfile' + i);
        document.getElementById("uploadfile0").parentNode.appendChild(clone);
    }
}
