$(function main()
{
    class Object
    {
        constructor(id, x, y)
        {
            this.id = id;
            this.x = x;
            this.y = y;
            this.class = "";
            this.additional = [];
        }
        changePosition(x, y)
        {
            this.x = x;
            this.y = y;
        }
        setClass(c)
        {
            this.class = c;
        }
        getClass()
        {
            return this.class;
        }
        getX()
        {
            return this.x;
        }
        getY()
        {
            return this.y;
        }
    }
    var id = 0;
    var xmlTab = [];
    var widget = [];
    var $table = $("#table");
    function addElementsToDivs(elem)
    {
        if ($(elem).hasClass('watch'))
        {
            elem.append('<table><tr><td>drag x: </td><td><input type="text" class="xPos" /></td></tr><tr><td>drag y: </td><td><input type="text" class="yPos" /></td></tr></table>');
        }
        else if ($(elem).hasClass('rss'))
        {
            elem.append('<p>Adres RSS: </p><input type="text" class="rssInput input"/>');
        }
        else if ($(elem).hasClass('weather'))
        {
            elem.append('<p>Podaj miejsce</p><input type="text" class="weatherInput input"/>');
        }
        else if ($(elem).hasClass('pictures'))
        {
            elem.append('<p>Podaj adress do albumu</p><input type="text" class="picturesInput input"/>')
        }
    }

    function checkClass(elem)
    {
        var $class = "";
        if ($(elem).hasClass('watch'))
        {
            $class = 'watch';
        }
        else if ($(elem).hasClass('rss'))
        {
            $class = 'rss';
        }
        else if ($(elem).hasClass('weather'))
        {
            $class = 'weather';
        }
        else if ($(elem).hasClass('pictures'))
        {
            $class = 'pictures';
        }
        return $class
    }
    function generateXML()
    {
        $(area).val("");
        var val = "";
        var $class = "";
        var x = "";
        var y = "";
        for (var i = 0; i < widget.length; i++)
        {
            $class = widget[i].getClass();
            x = widget[i].getX();
            y = widget[i].getY();
            if ($class == 'watch')
            {
                val = val + '<widget name="DateTimeWidget" x="' + x + '"+ y="' + y + '"></widget>';
            }
            else if ($class == 'rss')
            {
                val = val + '<widget name="RssWidget" x="' + x + '"+ y="' + y + '"></widget>';
            }
            else if ($class == 'weather')
            {
                val = val + '<widget name="WeathercastWidget" x="' + x + '"+ y="' + y + '"></widget>';
            }
            else if ($class == 'pictures')
            {
                val = val + '<widget name="ImageWidget" x="' + x + '"+ y="' + y + '"></widget>';
            }
            val = val + "\n";
        }
        return val;
    }
    var $startPostion = $("#firstdiv");
    var $element;
    var pos;
    $("#gen").click(function ()
    {
        $(area).val(generateXML());
    });
    $(".ob").draggable({
        helper: "clone",
        revert: "invalid"
    });


    $("#table").droppable({
        accept: ".ob",
        drop: function (event, ui)
        {
            var tab = $(this);
            drop(event, ui);
            var elem
            function drop(event, ui)
            {
                var left = "0";
                var $top = "0";
                var localID = id;
                var obiect = new Object(localID, left, $top);
                $(tab).append($(ui.draggable).clone());
                $("#table .ob").addClass("obiekt");
                $(".obiekt").removeClass("ui-draggable ob");
                $(".obiekt").draggable({
                    create: function (event, ui)
                    {
                        var id = localID;
                        elem = this;
                        $(elem).position({
                            my: "left top",
                            at: "left top",
                            of: $startPostion
                        });
                        // $(elem).data('$localIndex', $localIndex);

                        //---
                        obiect.setClass(checkClass($(elem)));
                        addElementsToDivs($(elem));
                        widget.push(obiect);
                        $(elem).append('<input type="button" class="delete" value="X"/>');
                        $(elem).children(".delete").position({
                            my: "right top",
                            at: "right top",
                            of: elem
                        });
                        $(elem).children(".delete").click(function ()
                        {
                            // xmlTab.splice($localIndex, 1);
                            for (var i = 0; i < widget.length; i++)
                            {
                                if (widget[i].id == localID)
                                {
                                    widget.splice(i, 1);
                                    break;
                                }
                            }
                            $(elem).closest(".obiekt").remove();
                        });
                    },
                    start: function ()
                    {
                        $element = this;

                    },
                    drag: function (event, ui)
                    {
                        pos = $(this).offset();
                        left = (pos.left - $startPostion.offset().left);
                        $top = (pos.top - $startPostion.offset().top);
                        $(".xPos", $element).val(left);
                        $(".yPos", $element).val($top);
                        $(".xD").val("left: " + left.toFixed(0) + " top: " + $top.toFixed(0));
                    },
                    containment: "#table",
                    stop: function (event, ui)
                    {
                        var x = left.toFixed(0);
                        var y = $top.toFixed(0);
                        for (var i = 0; i < widget.length; i++)
                        {
                            if (widget[i].id == localID)
                            {
                                widget[i].changePosition(x, y);
                                break;
                            }
                        }
                        //if ($index != 0) {
                        //    var $url = $(elem).children(".input").val();
                        //nowa tablica ze stringiem XMLowisim
                        // xmlTab[$index] = generateElementXML($(elem), $index, left, $top, $url);
                        //}
                    }

                });
                id = id + 1;
            }
        }
    });
});
