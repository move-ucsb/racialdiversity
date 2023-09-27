{
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "4gb7yr",
          "type": "geojson",
          "config": {
            "dataId": "h",
            "label": "LA",
            "color": [
              248,
              149,
              112
            ],
            "highlightColor": [
              252,
              242,
              26,
              255
            ],
            "columns": {
              "geojson": "geom"
            },
            "isVisible": true,
            "visConfig": {
              "opacity": 1,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                240,
                237,
                234
              ],
              "colorRange": {
                "name": "Uber Viz Qualitative 3",
                "type": "qualitative",
                "category": "Uber",
                "colors": [
                    "#66cc00",
                    "#99ff99",
                    "#ffff00",
                    "#ff6666",
                    "#ff9999",
                    "#9966ff",
                    "#cc99ff",
                    "#cccccc",
                    "#ff9900",
                    "#ffcc99",
                    "#99752e"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radius": 10,
              "sizeRange": [
                0,
                10
              ],
              "radiusRange": [
                0,
                50
              ],
              "heightRange": [
                0,
                500
              ],
              "elevationScale": 5,
              "enableElevationZoomFactor": true,
              "stroked": true,
              "filled": true,
              "enable3d": false,
              "wireframe": false
            },
            "hidden": false,
            "textLabel": [
              {
                "field": null,
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 18,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "category",
              "type": "string"
            },
            "colorScale": "ordinal",
            "strokeColorField": null,
            "strokeColorScale": "quantile",
            "sizeField": null,
            "sizeScale": "linear",
            "heightField": null,
            "heightScale": "linear",
            "radiusField": null,
            "radiusScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "6nj77rf1": [
              {
                "name": "name",
                "format": null
              },
              {
                "name": "category",
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
      "topLayerGroups": {
        "label": true
      },
      "visibleLayerGroups": {
        "label": true,
        "road": true,
        "border": false,
        "building": true,
        "water": true,
        "land": true
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