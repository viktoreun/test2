import streamlit
from streamlit_agraph import agraph, Node, Edge, Config, TripleStore

nodes = []
edges = []

#node 를 정의하고 - fixed 속성 추가
nodes.append(Node(id="spiderman",
                  label="Peter Parker",
                  size=25,
                  shape="circularImage",
                  image="https://upload.wikimedia.org/wikipedia/en/thumb/2/21/Web_of_Spider-Man_Vol_1_129-1.png/250px-Web_of_Spider-Man_Vol_1_129-1.png",
                  fixed=False)  # 노드가 물리 법칙에 따라 움직이도록
             )
nodes.append(Node(id="Captain_Marvel",
                  label="Carol Danvers",
                  size=25,
                  shape="circularImage",
                  image="https://cdn.marvel.com/content/2x/captainmarvel_lob_mas_mob_03_0.jpg",
                  fixed=False)
            )

nodes.append(Node(id="Hulk",
                  label="Bruce Banner",
                  size=25,
                  shape="circularImage",
                  image="https://cdn.marvel.com/content/2x/006hbb_ons_mas_mob_01_0.jpg",
                  fixed=False)
             )

## edge를 정의해서
edges.append(Edge(source="Captain_Marvel",
                  label="friend_of",
                  target="spiderman",
                  )
             )

edges.append(Edge(source="Hulk",
                  label="friend_of",
                  target="spiderman",
                  )
             )


config = Config(width=750,
                height=500,
                directed=True,
                hierarchical=False,
                nodeHighlightBehavior=True,
                physics_options = {
                    "physics": {
                        "enabled": True,
                        "barnesHut": {
                            "gravitationalConstant": -80000,
                            "centralGravity": 0.5,
                            "springLength": 200,
                            "springConstant": 0.001,  # 더 유연한 스프링
                            "damping": 0.01         # 적절한 댐핑
                        },
                        "stabilization": {
                            "enabled": True,
                            "iterations": 1000
                        },
                        "maxVelocity": 50,
                        "minVelocity": 0.75
                    },
                    "interaction": {
                        "dragNodes": True,
                        "dragView": True,
                        "zoomView": True,
                        "hover": True
                    }
                }
                                )

return_value = agraph(nodes=nodes,
                      edges=edges,
                      config=config)