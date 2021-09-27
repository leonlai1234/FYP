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