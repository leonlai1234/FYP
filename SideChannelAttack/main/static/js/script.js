var j = 0;

function duplicate() {
    if(j < 9){
        document.getElementById('addform').onclick = duplicate;
        var original = document.getElementById('uploadfile');
        var clone = original.cloneNode();
        j += 1;
        clone.removeAttribute('hidden');
        clone.setAttribute('name','uploadfile' + j);
        clone.setAttribute('id','uploadfile' + j);
        document.getElementById("uploadfile0").parentNode.appendChild(clone);
    }
}

function checkFiles(files,id){
    if(files.length>10){
        alert("10 pcap files per entries.");

        let list = new DataTransfer;
        for(let i=0; i<10; i++)
        {
            list.items.add(files[i]) 
        }
        document.getElementById(id).files = list.files
    }else if(files.length < 10){
        alert("10 pcap files per entries.");
    }
}