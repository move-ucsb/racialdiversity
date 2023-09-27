{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "hty62yd",
          "type": "point",
          "config": {
            "dataId": "h",
            "label": "LA",
            "color": [
              23,
              184,
              190
            ],
            "highlightColor": [
              252,
              242,
              26,
              255
            ],
            "columns": {
              "lat": "poi_lat",
              "lng": "poi_lng",
              "altitude": null
            },
            "isVisible": true,
            "visConfig": {
              "radius": 10,
              "fixedRadius": false,
              "opacity": 0.39,
              "outline": false,
              "thickness": 2,
              "strokeColor": [
                23,
                184,
                190
              ],
              "colorRange": {
                "name": "ColorBrewer PRGn-6",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                    "#4f9e00",
                    "#99ff99",
                    "#eb2f2f",
                    "#ff9999",
                    "#722ff7",
                    "#cc99ff",
                    "#d98200",
                    "#ffcc99",
                    "#949494"
                ],
                "reversed": false
              },
              "strokeColorRange": {
                "name": "ColorBrewer PRGn-6",
                "type": "diverging",
                "category": "ColorBrewer",
                "colors": [
                  "#762a83",
                  "#af8dc3",
                  "#e7d4e8",
                  "#d9f0d3",
                  "#7fbf7b",
                  "#1b7837"
                ],
                "reversed": false
              },
              "radiusRange": [
                4.2,
                94.3
              ],
              "filled": true
            },
            "hidden": false,
            "textLabel": []
          },
          "visualChannels": {
            "colorField": {
              "name": "class_dominant",
              "type": "string"
            },
            "colorScale": "ordinal",
            "strokeColorField": null,
            "strokeColorScale": "quantile",
            "sizeField": null,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "h": [
              {
                "name": "class_dominant",
                "format": null
              },
              {
                "name": "brand_name",
                "format": null
              },
              {
                "name": "sic_code",
                "format": null
              },
              {
                "name": "sic_name",
                "format": null
              },
              {
                "name": "scaled_entropy",
                "format": null
              }
            ]
          },
          "compareMode": false,
          "compareType": "absolute",
          "enabled": true
        },
        "brush": {
          "size": 0.5,
          "enabled": false
        },
        "geocoder": {
          "enabled": false
        },
        "coordinate": {
          "enabled": false
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": null,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": 0,
      "dragRotate": false,
      "latitude": 34.06172363981573,
      "longitude": -118.28896852464057,
      "pitch": 0,
      "zoom": 9.465284524851851,
      "isSplit": false
    },
    "mapStyle": {
      "styleType": "light",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "border": false,
        "building": true,
        "label": true,
        "land": true,
        "road": true,
        "water": true
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}