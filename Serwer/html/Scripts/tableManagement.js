$(function main() {
    //Przechowuje id,pozycję,klasę (i inne?)danego elementu. 
    class Object {
        //id - identyfikator elementu, 
        //x - wartość left() elementu,
        //y - watość top() elementu,
        //class - typ widgetu elementu (watch, clock, rss, itp.)
        //url - opcjonalny adres url przypisany do danego obiektu
        constructor(id, x, y) {
            this.id = id;
            this.x = x;
            this.y = y;
            this.class = "";
            this.url = "";
        }
        setPosition(x, y) {
            this.x = x;
            this.y = y;
        }
        setClass(c) {
            this.class = c;
        }
        getClass() {
            return this.class;
        }
        getX() {
            return this.x;
        }
        getY() {
            return this.y;
        }
        setUrl(url) {
            this.url = url;
        }
        getUrl() {
            return this.url;
        }
    }
    var id = 0;
    // var xmlTab = [];
    var widget = [];
    var $table = $("#table");

    //dodaje pola do danego elementu zależnie od posiadanej klasy
    function addElementsToDivs(elem) {
        if ($(elem).hasClass('watch')) {
        }
        else if ($(elem).hasClass('rss')) {
            elem.append('<p>Adres RSS: </p><input type="text" class="rssInput input"/><input type="button" class="confirm" value="Zatwierdź adres"/>');
        }
        else if ($(elem).hasClass('weather')) {
            elem.append('<p>Podaj miejsce</p><input type="text" class="weatherInput input"/><input type="button" class="confirm" value="Zatwierdź adres"/>');
        }
        else if ($(elem).hasClass('pictures')) {
            elem.append('<p>Podaj adress do albumu</p><input type="text" class="picturesInput input"/><input type="button" class="confirm" value="Zatwierdź adres"/>')
        }
        else if ($(elem).hasClass('http')) {
            elem.append('<p>Adres http: </p><input type="text" class="httpInput input"/><input type="button" class="confirm" value="Zatwierdź adres"/>');
        }
    }

    //sprawdza klasę parametru elem, i zwraca nazwę tej klasy
    function checkClass(elem) {
        var $class = "";
        if ($(elem).hasClass('watch')) {
            $class = 'watch';
        }
        else if ($(elem).hasClass('rss')) {
            $class = 'rss';
        }
        else if ($(elem).hasClass('weather')) {
            $class = 'weather';
        }
        else if ($(elem).hasClass('pictures')) {
            $class = 'pictures';
        }
        else if ($(elem).hasClass('http')) {
            $class = 'http';
        }
        return $class
    }
    function toPHP(xml) {
        var data = new FormData();
        data.append("data", xml);
        var xhr = (window.XMLHttpRequest) ? new XMLHttpRequest() : new activeXObject("Microsoft.XMLHTTP");
        xhr.open('post', 'http://137.74.42.193/saveFile.php', true);
        xhr.send(data);
    }

    //zwraca xml według danego wzorca, z obiektów typu Object przechowywanych w tablicy widget, 

    function generateXML() {
        $(area).val("");
        var val = '<?xml version="1.0" encoding="utf-8" ?>\n<table>\n<page>\n';
        var $class = "";
        var x = "";
        var y = "";
        var url = "";
        for (var i = 0; i < widget.length; i++) {
            $class = widget[i].getClass();
            x = widget[i].getX();
            y = widget[i].getY();
            url = widget[i].getUrl();
            if ($class == 'watch') {
                val = val + '<widget name="DateTimeWidget" x="' + x + '" y="' + y + '"></widget>';
            }
            else if ($class == 'rss') {
                val = val + '<widget name="RssWidget" x="' + x + '" y="' + y + '" url="' + url + '"></widget>';
            }
            else if ($class == 'weather') {
                val = val + '<widget name="WeathercastWidget" x="' + x + '" y="' + y + '" url="' + url + '"></widget>';
            }
            else if ($class == 'pictures') {
                val = val + '<widget name="ImageWidget" x="' + x + '" y="' + y + '" url="' + url + '"></widget>';
            }
            else if ($class == 'http') {
                val = val + '<widget name="HtmlWidget" x="' + x + '" y="' + y + '" url="' + url + '"></widget>';
            }
            val = val + "\n";
        }
        return val+"</page>\n</table>";
    }
    var $startPostion = $("#firstdiv");
    var $element;
    var pos;
    $("#gen").click(function () {
        var generatedXML = generateXML();
        $(area).val(generatedXML);
        toPHP(generatedXML);
    });
    //metoda draggable dla elemetów znajdujących się na liście
    $(".ob").draggable({
        helper: "clone",
        revert: "invalid"
    });

    //główna metoda służąca w zarządzaniu elementami  
    $("#table").droppable({
        accept: ".ob",
        drop: function (event, ui) {
            var tab = $(this);
            drop(event, ui);
            var elem
            function drop(event, ui) {
                var left = "0";
                var $top = "0";
                var obiect = new Object(id, left, $top);
                $(tab).append($(ui.draggable).clone());
                $("#table .ob").addClass("obiekt");
                $(".obiekt").removeClass("ui-draggable ob");
                $(".obiekt").draggable({
                    create: function (event, ui) {
                        elem = this;
                        $(elem).position({
                            my: "left top",
                            at: "left top",
                            of: $startPostion
                        });
                        obiect.setClass(checkClass($(elem)));
                        addElementsToDivs($(elem));
                        widget.push(obiect);
                        $(elem).append('<input type="button" class="delete" value="X"/>');
                        jQuery(elem).attr("id", id);
                        var localID = $(elem).attr("id");
                        $(elem).children(".delete").position({
                            my: "right top",
                            at: "right top",
                            of: elem
                        });
                        $(elem).children(".delete").click(function () {
                            // xmlTab.splice($localIndex, 1);
                            for (var i = 0; i < widget.length; i++) {
                                if (widget[i].id == localID) {
                                    widget.splice(i, 1);
                                    break;
                                }
                            }
                            $(elem).closest(".obiekt").remove();
                        });
                        $(elem).children(".confirm").click(function () {
                            for (var i = 0; i < widget.length; i++) {
                                if (widget[i].id == localID) {
                                    widget[i].setUrl($(elem).children(".input").val());
                                    break;
                                }
                            }
                        })
                    },
                    start: function () {
                        $element = this;

                    },
                    drag: function (event, ui) {
                        pos = $(this).offset();
                        left = (pos.left - $startPostion.offset().left);
                        $top = (pos.top - $startPostion.offset().top);
                        $(".xPos", $element).val(left);
                        $(".yPos", $element).val($top);
                        $(".xD").val("left: " + left.toFixed(0) + " top: " + $top.toFixed(0));
                    },
                    containment: "#table",
                    stop: function (event, ui) {
                        var x = left.toFixed(0);
                        var y = $top.toFixed(0);
                        for (var i = 0; i < widget.length; i++) {
                            if (widget[i].id == $(this).attr("id")) {
                                widget[i].setPosition(x, y);
                                break;
                            }
                        }
                    }

                });
                id = id + 1;
            }
        }
    });
});
