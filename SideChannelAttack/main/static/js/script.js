var j = 0;
var k = 0;

function duplicate() {
    if(j < 9){
        document.getElementById('addform').onclick = duplicate;
        var original = document.getElementById('uploadfile');
        var clone = original.cloneNode();
        j += 1;
        clone.removeAttribute('hidden');
        clone.setAttribute('required','required');
        clone.setAttribute('name','uploadfile' + j);
        clone.setAttribute('id','uploadfile' + j);
        document.getElementById("uploadfile0").parentNode.appendChild(clone);
    }
}

function filevalidation(files,id){
    var fileInput = document.getElementById(id);      
    var filePath = fileInput.value;

    // Allowing file type
    var allowedExtensions = /(\.pcap)$/i;
        
    if (!allowedExtensions.exec(filePath)) {
        alert('Invalid file type. Please choose PCAP files only.');
        fileInput.value = '';
        return false;
    }
    
    if(files.length>10){
        alert("10 pcap files per entries.");

        let list = new DataTransfer;
        for(let i=0; i<10; i++)
        {
            list.items.add(files[i]) 
        }
        document.getElementById(id).files = list.files
        return false;
    } 
    
    if(files.length < 10){
        alert("10 pcap files per entries.");
        fileInput = document.getElementById(id);
        filePath = fileInput.value;
        fileInput.value = '';
        return false;
    }
}

function remove(){
    for(j ;j > 0;j--){
        var obj = document.getElementById("uploadfile" + j);
        obj.remove();
    }
    j = 0;
}