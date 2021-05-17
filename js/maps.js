function iniciarMap(){
    var coord = {lat:-33.58576648345951,lng:-70.58041738493148};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 17,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}