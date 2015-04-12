function create_map(obj, url) {
    var mapOptions = {
        center: {
            lat: 52,
            lng: 20
        },
        zoom: 6,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
    };
    var map = new google.maps.Map(obj, mapOptions);
    var json = (function() {
        var json = null;
        $.ajax({
            'async': false,
            'global': false,
            'url': url,
            'dataType': "json",
            'success': function(data) {
                json = data;
            }
        });
        return json;
    })();
    for (var i = 0, length = json.results.length; i < length; i++) {
        var data = json.results[i];
        console.log(data);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(data.lat, data.lng),
            map: map,
            title: data.title,
        });
        infoBox(map, marker, data);
    };
}

function infoBox(map, marker, data) {
    var infoWindow = new google.maps.InfoWindow();
    console.log(data);
    google.maps.event.addListener(marker, "click", function(e) {
            infoWindow.setContent("<a href='"+data.get_absolute_url+"'>"+data.title+"</a>");
            infoWindow.open(map, marker);
    });
}

function init_map(id, url) {
    google.maps.event.addDomListener(window, 'load', function() {
        create_map(id, url);
    });
};
