(* Generic graph searching using OCaml. Two interesting functions are below. *)

exception NotImplemented
exception Fail

(* The type of graphs. *)
type 'a graph = {
  nodes: 'a list;
  edges: ('a * 'a) list
}


(* Consider a function that, given a graph and a node that is in that graph,
returns a list of that node's out-neighbours. Recall that a node v2 is an
out-neighbour of node v1 if an edge (v1, v2) exists in the graph. That is, 
there exists a directed edge from v1 to v2.
The function *)
let neighbours g vertex = 
  List.map snd (List.filter (fun (x,y) -> x = vertex) (g.edges))


(*Now consider a function that, given a graph g and two nodes a and b in the graph, 
returns a path (a list of nodes to visit, in order) from a to b. The path includes both the endpoints.
If no possible path exists, we raise the exception Fail. Furthermore, we implement this function
using backtracking and we ensure that no cycles are present in the path.
The function: *)
let find_path (g : 'a graph) (a : 'a) (b : 'a) =
  let rec aux_node (node : 'a) (visited : 'a list) =
    if b = node then [b] else
    if List.mem (node) (visited) then raise Fail
    else node::
         (aux_list (neighbours g node) (node::visited))

  and aux_list (nodes : 'a list) (visited : 'a list) = match nodes with
    | [] -> raise Fail
    | hd :: tl -> try aux_node (hd) (visited) with
      | Fail -> aux_list (tl) (visited) 
  in
  aux_node a []
