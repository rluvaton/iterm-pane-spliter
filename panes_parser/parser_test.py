import unittest

from panes_parser.panes_tree import TreeNode, Size, SplitNode, TreeLeaf
from panes_parser.parser import convert_pane_structures_to_tree

class TestPanesParser(unittest.TestCase):

    def test_should_not_split(self):
        test_cases = [
            {'paneStructure': [[1]]},
            {'paneStructure': [[1, 1], [1, 1]]},
            {'paneStructure': [[1, 1, 1], [1, 1, 1]]},
        ]

        for idx, case in enumerate(test_cases):
            with self.subTest(case=case):
                pane_structure = case['paneStructure']
                expected_result = TreeNode(
                    node_id=pane_structure[0][0],
                    size=Size(
                        height=len(pane_structure),
                        width=len(pane_structure[0])
                    )
                )
                self.assertEqual(
                    convert_pane_structures_to_tree(pane_structure),
                    expected_result
                )

    def test_simple_single_split_vertical(self):
        pane_structure = [[1, 2]]

        expected_result = SplitNode(
            split_type='right',
            size=Size(height=1, width=2),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=1, width=1)
                ),
                TreeLeaf(
                    node_id=2,
                    size=Size(height=1, width=1)
                )
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_simple_multi_split_vertical(self):
        pane_structure = [
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
            [1, 2],
        ]

        expected_result = SplitNode(
            split_type='right',
            size=Size(height=5, width=2),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=5, width=1)
                ),
                TreeLeaf(
                    node_id=2,
                    size=Size(height=5, width=1)
                ),
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_simple_multi_split_vertical_2(self):
        pane_structure = [
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
        ]

        expected_result = SplitNode(
            split_type='right',
            size=Size(height=5, width=4),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=5, width=1)
                ),

                SplitNode(
                    split_type='right',
                    size=Size(height=5, width=3),
                    splits=[
                        TreeLeaf(
                            node_id=2,
                            size=Size(height=5, width=1)
                        ),
                        SplitNode(
                            split_type='right',
                            size=Size(height=5, width=2),
                            splits=[
                                TreeLeaf(
                                    node_id=3,
                                    size=Size(height=5, width=1)
                                ),
                                TreeLeaf(
                                    node_id=4,
                                    size=Size(height=5, width=1)
                                )
                            ]
                        ),
                    ]
                ),
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_simple_multi_split_vertical_3(self):
        pane_structure = [
            [1, 2, 3, 3],
            [1, 2, 3, 3],
            [1, 2, 3, 3],
            [1, 2, 3, 3],
            [1, 2, 3, 3],
        ]

        expected_result = SplitNode(
            split_type='right',
            size=Size(height=5, width=4),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=5, width=1)
                ),
                SplitNode(
                    split_type='right',
                    size=Size(height=5, width=3),
                    splits=[
                        TreeLeaf(
                            node_id=2,
                            size=Size(height=5, width=1)
                        ),
                        TreeLeaf(
                            node_id=3,
                            size=Size(height=5, width=2)
                        )
                    ]
                ),
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_simple_single_split_horizontal(self):
        pane_structure = [
            [1],
            [2],
        ]

        expected_result = SplitNode(
            split_type='bottom',
            size=Size(height=2, width=1),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=1, width=1)
                ),
                TreeLeaf(
                    node_id=2,
                    size=Size(height=1, width=1)
                )
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_simple_multi_split_horizontal(self):
        pane_structure = [
            [1, 1, 1, 1],
            [2, 2, 2, 2],
        ]

        expected_result = SplitNode(
            split_type='bottom',
            size=Size(height=2, width=4),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=1, width=4)
                ),
                TreeLeaf(
                    node_id=2,
                    size=Size(height=1, width=4)
                )
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_simple_multi_split_horizontal_2(self):
        pane_structure = [
            [1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3],
            [4, 4, 4, 4],
            [5, 5, 5, 5],
        ]

        expected_result = SplitNode(
            split_type='bottom',
            size=Size(height=5, width=4),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=1, width=4)
                ),
                SplitNode(
                    split_type='bottom',
                    size=Size(height=4, width=4),
                    splits=[
                        TreeLeaf(
                            node_id=2,
                            size=Size(height=1, width=4)
                        ),
                        SplitNode(
                            split_type='bottom',
                            size=Size(height=3, width=4),
                            splits=[
                                TreeLeaf(
                                    node_id=3,
                                    size=Size(height=1, width=4)
                                ),
                                SplitNode(
                                    split_type='bottom',
                                    size=Size(height=2, width=4),
                                    splits=[
                                        TreeLeaf(
                                            node_id=4,
                                            size=Size(height=1, width=4)
                                        ),
                                        TreeLeaf(
                                            node_id=5,
                                            size=Size(height=1, width=4)
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_simple_multi_split_horizontal_3(self):
        pane_structure = [
            [1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3],
            [3, 3, 3, 3],
        ]

        expected_result = SplitNode(
            split_type='bottom',
            size=Size(height=4, width=4),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=1, width=4)
                ),
                SplitNode(
                    split_type='bottom',
                    size=Size(height=3, width=4),
                    splits=[
                        TreeLeaf(
                            node_id=2,
                            size=Size(height=1, width=4)
                        ),
                        TreeLeaf(
                            node_id=3,
                            size=Size(height=2, width=4)
                        )
                    ]
                )
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_complex_splits_1(self):
        pane_structure = [
            [1, 2],
            [1, 3],
        ]

        expected_result = SplitNode(
            split_type='right',
            size=Size(height=2, width=2),
            splits=[
                TreeLeaf(
                    node_id=1,
                    size=Size(height=2, width=1)
                ),
                SplitNode(
                    split_type='bottom',
                    size=Size(height=2, width=1),
                    splits=[
                        TreeLeaf(
                            node_id=2,
                            size=Size(height=1, width=1)
                        ),
                        TreeLeaf(
                            node_id=3,
                            size=Size(height=1, width=1)
                        )
                    ]
                )
            ]
        )

        self.assertEqual(
            convert_pane_structures_to_tree(pane_structure),
            expected_result
        )

    def test_complex_splits_2(self):
        pane_structure = [
            [1, 2],
            [3, 4],
        ]

        possible_solutions = [
            SplitNode(
                split_type='right',
                size=Size(height=2, width=2),
                splits=[
                    SplitNode(
                        split_type='bottom',
                        size=Size(height=2, width=1),
                        splits=[
                            TreeLeaf(
                                node_id=1,
                                size=Size(height=1, width=1)
                            ),
                            TreeLeaf(
                                node_id=3,
                                size=Size(height=1, width=1)
                            )
                        ]
                    ),
                    SplitNode(
                        split_type='bottom',
                        size=Size(height=2, width=1),
                        splits=[
                            TreeLeaf(
                                node_id=2,
                                size=Size(height=1, width=1)
                            ),
                            TreeLeaf(
                                node_id=4,
                                size=Size(height=1, width=1)
                            )
                        ]
                    ),
                ]
            ),
            SplitNode(
                split_type='bottom',
                size=Size(height=2, width=2),
                splits=[
                    SplitNode(
                        split_type='right',
                        size=Size(height=1, width=2),
                        splits=[
                            TreeLeaf(
                                node_id=1,
                                size=Size(height=1, width=1)
                            ),
                            TreeLeaf(
                                node_id=2,
                                size=Size(height=1, width=1)
                            )
                        ]
                    ),
                    SplitNode(
                        split_type='right',
                        size=Size(height=1, width=2),
                        splits=[
                            TreeLeaf(
                                node_id=3,
                                size=Size(height=1, width=1)
                            ),
                            TreeLeaf(
                                node_id=4,
                                size=Size(height=1, width=1)
                            )
                        ]
                    )
                ]
            )
        ]

        tree = convert_pane_structures_to_tree(pane_structure)
        try:
            self.assertEqual(
                tree,
                possible_solutions[0]
            )
        except:
            self.assertEqual(
                tree,
                possible_solutions[1]
            )

    def test_complex_splits_3(self):
        pane_structure = [
            [1, 1, 5],
            [2, 7, 5],
            [2, 7, 3],
            [2, 8, 6],
            [4, 4, 4],
        ]

        expected_result = SplitNode(
            split_type='bottom',
            size=Size(height=5, width=3),
            splits=[
                SplitNode(
                    # [1, 1, 5],
                    # [2, 7, 5],
                    # [2, 7, 3],
                    # [2, 8, 6],

                    split_type='right',
                    size=Size(height=4, width=3),
                    splits=[
                        SplitNode(

                            # [1, 1],
                            # [2, 7],
                            # [2, 7],
                            # [2, 8],
                            split_type='bottom',
                            size=Size(height=4, width=2),
                            splits=[
                                TreeLeaf(
                                    # [1, 1],
                                    node_id=1,
                                    size=Size(height=1, width=2)
                                ),
                                SplitNode(
                                    # [2, 7],
                                    # [2, 7],
                                    # [2, 8],
                                    split_type='right',
                                    size=Size(height=3, width=2),
                                    splits=[
                                        TreeLeaf(
                                            # [2],
                                            # [2],
                                            # [2],
                                            node_id=2,
                                            size=Size(height=3, width=1)
                                        ),
                                        SplitNode(
                                            # [7],
                                            # [7],
                                            # [8],
                                            split_type='bottom',
                                            size=Size(height=3, width=1),
                                            splits=[
                                                TreeLeaf(
                                                    # [7],
                                                    # [7],
                                                    node_id=7,
                                                    size=Size(height=2, width=1)
                                                ),
                                                TreeLeaf(
                                                    # [8],
                                                    node_id=8,
                                                    size=Size(height=1, width=1)
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        SplitNode(
                            # [5],
                            # [5],
                            # [3],
                            # [6],
                            split_type='bottom',
                            size=Size(height=4, width=1),
                            splits=[
                                TreeLeaf(
                                    # [5],
                                    # [5],
                                    node_id=5,
                                    size=Size(height=2, width=1)
                                ),
                                SplitNode(
                                    # [3],
                                    # [6],
                                    split_type='bottom',
                                    size=Size(height=2, width=1),
                                    splits=[
                                        TreeLeaf(
                                            # [3],
                                            node_id=3,
                                            size=Size(height=1, width=1)
                                        ),
                                        TreeLeaf(
                                            # [6],
                                            node_id=6,
                                            size=Size(height=1, width=1)
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                TreeLeaf(
                    # [4, 4, 4],
                    node_id=4,
                    size=Size(height=1, width=3)
                )
            ]
        )

        tree = convert_pane_structures_to_tree(pane_structure)
        self.assertEqual(
            tree,
            expected_result
        )


if __name__ == '__main__':
    unittest.main()
