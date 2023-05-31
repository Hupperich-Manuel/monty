use monty::{Executor, Exit};

/// macro for expected values
macro_rules! expect_ok_or_error {
    ($name:ident, ok, $code:literal, $expected:expr) => {
        paste::item! {
            #[test]
            fn [< expect_ $name _ok >]() {
                let ex = Executor::new($code, "test.py", &[]).unwrap();
                let output = match ex.run(vec![]) {
                    Ok(Exit::Return(value)) => format!("{:?}", value),
                    otherwise => panic!("Unexpected exit: {:?}", otherwise),
                };
                let expected = $expected.trim_matches('\n');
                assert_eq!(output, expected);
            }
        }
    };
    ($name:ident, err, $code:literal, $error:expr) => {
        paste::item! {
            #[test]
            fn [< expect_ $name _ $error:snake _error >]() {
                todo!("implement err test")
            }
        }
    };
}

/// macro to define many tests for expected values
macro_rules! execute_tests {
    ($($name:ident: $ok_or_err:ident => $code:literal, $expected:expr;)*) => {
        $(
            expect_ok_or_error!($name, $ok_or_err, $code, $expected);
        )*
    }
}


execute_tests! {
    add_ints: ok => "1 + 1", "Int(2)";
    add_strs: ok => "'a' + 'b'", r#"Str("ab")"#;
    for_loop_str_append: ok => r#"
v = ''
for i in range(1000):
    if i % 13 == 0:
        v += 'x'
len(v)
"#, "Int(77)";
}
