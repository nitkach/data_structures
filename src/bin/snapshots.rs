pub fn nesting() -> &'static str {
    r#"
                ├──x
                │  ├──x
                │  │  ├──x *
                │  │  ├──y *
                │  │  └──z *
                │  ├──y
                │  │  ├──x *
                │  │  ├──y *
                │  │  └──z *
                │  └──z
                │     ├──x *
                │     ├──y *
                │     └──z *
                ├──y
                │  ├──x
                │  │  ├──x *
                │  │  ├──y *
                │  │  └──z *
                │  ├──y
                │  │  ├──x *
                │  │  ├──y *
                │  │  └──z *
                │  └──z
                │     ├──x *
                │     ├──y *
                │     └──z *
                └──z
                   ├──x
                   │  ├──x *
                   │  ├──y *
                   │  └──z *
                   ├──y
                   │  ├──x *
                   │  ├──y *
                   │  └──z *
                   └──z
                      ├──x *
                      ├──y *
                      └──z *
            "#
}


fn main() {
    let seq = "xyz";
    for i in seq.chars() {
        for j in seq.chars() {
            for k in seq.chars() {
                print!("\"{i}{j}{k}\", ")
            }
        }
    }
}
